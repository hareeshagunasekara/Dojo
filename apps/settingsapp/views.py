from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserPreferencesForm, NotificationSettingsForm

@login_required
def settings_view(request):
    return render(request, 'settingsapp/settings.html')

@login_required
def preferences(request):
    if request.method == 'POST':
        form = UserPreferencesForm(request.POST)
        if form.is_valid():
            # Here you would typically save the preferences to a user profile model
            # For now, we'll just show a success message
            messages.success(request, 'Preferences updated successfully!')
            return redirect('settingsapp:preferences')
    else:
        form = UserPreferencesForm()
    
    return render(request, 'settingsapp/preferences.html', {'form': form})

@login_required
def notifications(request):
    if request.method == 'POST':
        form = NotificationSettingsForm(request.POST)
        if form.is_valid():
            # Here you would typically save the notification settings to a user profile model
            # For now, we'll just show a success message
            messages.success(request, 'Notification settings updated successfully!')
            return redirect('settingsapp:notifications')
    else:
        form = NotificationSettingsForm()
    
    return render(request, 'settingsapp/notifications.html', {'form': form})
