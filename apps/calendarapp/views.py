from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime
from .models import Event
from .forms import EventForm
from apps.settingsapp.models import UserSettings

@login_required
def calendar_view(request):
    events = Event.objects.filter(user=request.user)
    
    # Get user's week start preference
    try:
        user_settings = UserSettings.objects.get(user=request.user)
        week_start = user_settings.default_week_start
    except UserSettings.DoesNotExist:
        week_start = 'monday'  # Default to Monday
    
    context = {
        'events': events,
        'week_start': week_start
    }
    return render(request, 'calendarapp/calendar.html', context)

@login_required
@require_http_methods(["POST"])
def add_event_ajax(request):
    """Handle AJAX event creation"""
    try:
        form = EventForm(request.POST, user=request.user)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            
            # Handle all-day events
            if event.is_all_day:
                event.start_time = None
                event.end_time = None
            
            event.save()
            
            # Format start and end times for FullCalendar
            start_str = f"{event.start_date}" + (f"T{event.start_time}" if event.start_time else "")
            end_str = f"{event.end_date}" + (f"T{event.end_time}" if event.end_time else "")
            
            return JsonResponse({
                'success': True,
                'event': {
                    'id': event.id,
                    'title': event.title,
                    'start': start_str,
                    'end': end_str,
                    'description': event.description,
                    'location': event.location,
                    'event_type': event.event_type,
                    'is_all_day': event.is_all_day,
                    'course_name': event.course.name if event.course else None
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

@login_required
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            messages.success(request, 'Event added successfully!')
            return redirect('calendarapp:calendar_view')
    else:
        form = EventForm()
    
    return render(request, 'calendarapp/add_event.html', {'form': form})

@login_required
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id, user=request.user)
    return render(request, 'calendarapp/event_detail.html', {'event': event})

@login_required
def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id, user=request.user)
    
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event updated successfully!')
            return redirect('calendarapp:event_detail', event_id=event.id)
    else:
        form = EventForm(instance=event)
    
    return render(request, 'calendarapp/edit_event.html', {'form': form, 'event': event})

@login_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id, user=request.user)
    event.delete()
    messages.success(request, 'Event deleted successfully!')
    return redirect('calendarapp:calendar_view')

@login_required
@require_http_methods(["POST"])
def delete_event_ajax(request, event_id):
    """Handle AJAX event deletion"""
    try:
        event = get_object_or_404(Event, id=event_id, user=request.user)
        event.delete()
        return JsonResponse({
            'success': True,
            'message': 'Event deleted successfully!'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        })

@login_required
@require_http_methods(["POST"])
def update_event_ajax(request, event_id):
    """Handle AJAX event updates (drag and drop, resize)"""
    try:
        event = get_object_or_404(Event, id=event_id, user=request.user)
        data = json.loads(request.body)
        
        # Update start date and time
        if 'start_date' in data:
            event.start_date = datetime.strptime(data['start_date'], '%Y-%m-%d').date()
        if 'start_time' in data:
            event.start_time = datetime.strptime(data['start_time'], '%H:%M:%S').time()
        
        # Update end date and time
        if 'end_date' in data:
            event.end_date = datetime.strptime(data['end_date'], '%Y-%m-%d').date()
        if 'end_time' in data:
            event.end_time = datetime.strptime(data['end_time'], '%H:%M:%S').time()
        
        event.save()
        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        })
