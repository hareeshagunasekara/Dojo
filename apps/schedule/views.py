from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ClassSchedule
from .forms import ClassScheduleForm

@login_required
def schedule_view(request):
    classes = ClassSchedule.objects.filter(user=request.user)
    
    # Group classes by day
    schedule = {}
    for day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        schedule[day] = classes.filter(day_of_week=day)
    
    return render(request, 'schedule/schedule.html', {'schedule': schedule})

@login_required
def add_class(request):
    if request.method == 'POST':
        form = ClassScheduleForm(request.POST)
        if form.is_valid():
            class_schedule = form.save(commit=False)
            class_schedule.user = request.user
            class_schedule.save()
            messages.success(request, 'Class added to schedule successfully!')
            return redirect('schedule:schedule_view')
    else:
        form = ClassScheduleForm()
    
    return render(request, 'schedule/add_class.html', {'form': form})

@login_required
def edit_class(request, class_id):
    class_schedule = get_object_or_404(ClassSchedule, id=class_id, user=request.user)
    
    if request.method == 'POST':
        form = ClassScheduleForm(request.POST, instance=class_schedule)
        if form.is_valid():
            form.save()
            messages.success(request, 'Class schedule updated successfully!')
            return redirect('schedule:schedule_view')
    else:
        form = ClassScheduleForm(instance=class_schedule)
    
    return render(request, 'schedule/edit_class.html', {'form': form, 'class_schedule': class_schedule})

@login_required
def delete_class(request, class_id):
    class_schedule = get_object_or_404(ClassSchedule, id=class_id, user=request.user)
    class_schedule.delete()
    messages.success(request, 'Class removed from schedule successfully!')
    return redirect('schedule:schedule_view')
