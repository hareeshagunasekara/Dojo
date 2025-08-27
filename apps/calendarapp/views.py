from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event
from .forms import EventForm

@login_required
def calendar_view(request):
    events = Event.objects.filter(user=request.user)
    return render(request, 'calendarapp/calendar.html', {'events': events})

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
