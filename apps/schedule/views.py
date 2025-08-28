from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.forms import modelformset_factory
from datetime import datetime, timedelta
from .models import ClassSchedule, ScheduleSlot
from .forms import ClassScheduleForm, ScheduleSlotFormSet, ScheduleSlotForm

@login_required
def schedule_view(request):
    """Main schedule view showing 7-day timetable"""
    today = datetime.now()
    
    # Get all schedules for the current user
    schedules = ClassSchedule.objects.filter(user=request.user).prefetch_related('slots')
    
    # Create a 7-day timetable structure
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    # Get today's day name for highlighting
    today_day = today.strftime('%A').lower()
    today_index = days.index(today_day) if today_day in days else 0
    
    # Organize slots by day
    timetable = {}
    for day in days:
        timetable[day] = []
    
    for schedule in schedules:
        for slot in schedule.slots.all():
            if slot.day_of_week in timetable:
                # Calculate position based on start time (assuming 24-hour format)
                start_hour = slot.start_time.hour
                start_minute = slot.start_time.minute
                
                # Convert to minutes since midnight for easier calculation
                minutes_since_midnight = start_hour * 60 + start_minute
                
                # Calculate top position (assuming 6 AM to 10 PM = 16 hours = 960 minutes)
                # Start at 6 AM (360 minutes) and end at 10 PM (1320 minutes)
                # Scale to fit in 1200px height
                start_time_minutes = 360  # 6 AM
                end_time_minutes = 1320   # 10 PM
                total_minutes = end_time_minutes - start_time_minutes
                
                if minutes_since_midnight < start_time_minutes:
                    top_position = 0
                elif minutes_since_midnight > end_time_minutes:
                    top_position = 1200
                else:
                    top_position = ((minutes_since_midnight - start_time_minutes) / total_minutes) * 1200
                
                timetable[slot.day_of_week].append({
                    'schedule': schedule,
                    'slot': slot,
                    'color': schedule.color,
                    'title': schedule.title,
                    'instructor': schedule.instructor,
                    'room': schedule.room_location,
                    'time_range': f"{slot.start_time.strftime('%H:%M')} - {slot.end_time.strftime('%H:%M')}",
                    'top_position': top_position
                })
    
    # Sort slots by start time for each day
    for day in timetable:
        timetable[day].sort(key=lambda x: x['slot'].start_time)
    
    context = {
        'schedules': schedules,
        'timetable': timetable,
        'days': days,
        'day_names': day_names,
        'today_index': today_index,
        'today': today,
    }
    
    return render(request, 'schedule/schedule.html', context)

@login_required
def add_schedule(request):
    """Add new schedule with multiple slots"""
    if request.method == 'POST':
        schedule_form = ClassScheduleForm(request.POST, user=request.user)
        
        if schedule_form.is_valid():
            schedule = schedule_form.save(commit=False)
            schedule.user = request.user
            schedule.save()
            
            print(f"Schedule saved: {schedule}")
            
            # Process custom day selections and create slots
            slots_created = 0
            total_forms = int(request.POST.get('slots-TOTAL_FORMS', 0))
            
            print(f"Processing {total_forms} slot forms")
            print(f"POST data keys: {list(request.POST.keys())}")
            
            for i in range(total_forms):
                # Check which days are selected for this slot
                selected_days = []
                for day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
                    day_key = f'days_{day}_{i}'
                    if request.POST.get(day_key):
                        selected_days.append(day)
                        print(f"Day {day} selected for slot {i}")
                
                # Get time values
                start_time = request.POST.get(f'slots-{i}-start_time')
                end_time = request.POST.get(f'slots-{i}-end_time')
                
                print(f"Slot {i}: days={selected_days}, start={start_time}, end={end_time}")
                
                if start_time and end_time and selected_days:
                    # Create a slot for each selected day
                    for day in selected_days:
                        slot = ScheduleSlot(
                            schedule=schedule,
                            day_of_week=day,
                            start_time=start_time,
                            end_time=end_time,
                            order=slots_created
                        )
                        slot.save()
                        slots_created += 1
                        print(f"Created slot: {slot}")
                else:
                    print(f"Skipping slot {i} - missing data")
            
            print(f"Total slots created: {slots_created}")
            messages.success(request, 'Schedule created successfully!')
            return redirect('schedule:schedule_view')
        else:
            # If form is invalid, show errors
            print("Form errors:", schedule_form.errors)
            print("POST data:", request.POST)
    else:
        schedule_form = ClassScheduleForm(user=request.user)
    
    context = {
        'schedule_form': schedule_form,
        'slot_formset': ScheduleSlotFormSet(prefix='slots'),
        'today': datetime.now(),
    }
    
    return render(request, 'schedule/add_schedule.html', context)

@login_required
def edit_schedule(request, schedule_id):
    """Edit existing schedule"""
    schedule = get_object_or_404(ClassSchedule, id=schedule_id, user=request.user)
    
    if request.method == 'POST':
        schedule_form = ClassScheduleForm(request.POST, instance=schedule, user=request.user)
        slot_formset = ScheduleSlotFormSet(
            request.POST, 
            prefix='slots',
            queryset=schedule.slots.all()
        )
        
        if schedule_form.is_valid() and slot_formset.is_valid():
            schedule_form.save()
            
            # Save slots
            slots = slot_formset.save(commit=False)
            for i, slot in enumerate(slots):
                slot.schedule = schedule
                slot.order = i
                slot.save()
            
            # Delete marked slots
            slot_formset.save_existing_objects(commit=True)
            slot_formset.save_new_objects(commit=True)
            
            messages.success(request, 'Schedule updated successfully!')
            return redirect('schedule:schedule_view')
    else:
        schedule_form = ClassScheduleForm(instance=schedule, user=request.user)
        slot_formset = ScheduleSlotFormSet(
            prefix='slots',
            queryset=schedule.slots.all()
        )
    
    context = {
        'schedule': schedule,
        'schedule_form': schedule_form,
        'slot_formset': slot_formset,
        'today': datetime.now(),
    }
    
    return render(request, 'schedule/edit_schedule.html', context)

@login_required
def delete_schedule(request, schedule_id):
    """Delete schedule"""
    schedule = get_object_or_404(ClassSchedule, id=schedule_id, user=request.user)
    schedule.delete()
    messages.success(request, 'Schedule deleted successfully!')
    return redirect('schedule:schedule_view')

@login_required
@require_http_methods(["POST"])
def add_slot_ajax(request, schedule_id):
    """AJAX endpoint to add a slot to existing schedule"""
    try:
        schedule = get_object_or_404(ClassSchedule, id=schedule_id, user=request.user)
        form = ScheduleSlotForm(request.POST)
        
        if form.is_valid():
            slot = form.save(commit=False)
            slot.schedule = schedule
            slot.order = schedule.slots.count()
            slot.save()
            
            return JsonResponse({
                'success': True,
                'slot': {
                    'id': slot.id,
                    'day': slot.get_day_of_week_display(),
                    'start_time': slot.start_time.strftime('%H:%M'),
                    'end_time': slot.end_time.strftime('%H:%M'),
                }
            })
        else:
            return JsonResponse({
                'success': False,
                'errors': form.errors
            })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        })
