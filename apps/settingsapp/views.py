from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse
from .forms import UserPreferencesForm, NotificationSettingsForm, UserSettingsForm, DeleteAccountForm
from .models import UserSettings

@login_required
def settings_view(request):
    # Get or create user settings
    user_settings, created = UserSettings.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = UserSettingsForm(request.POST, instance=user_settings)
        if form.is_valid():
            form.save()
            messages.success(request, 'Settings updated successfully!')
            return redirect('settingsapp:settings_view')
    else:
        form = UserSettingsForm(instance=user_settings)
    
    context = {
        'form': form,
        'user_settings': user_settings
    }
    return render(request, 'settingsapp/settings.html', context)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password changed successfully!')
            return redirect('settingsapp:settings_view')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, 'settingsapp/change_password.html', {'form': form})

@login_required
def delete_account(request):
    if request.method == 'POST':
        form = DeleteAccountForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            user = authenticate(username=request.user.username, password=password)
            
            if user is not None:
                # Delete user settings first
                try:
                    user_settings = UserSettings.objects.get(user=user)
                    user_settings.delete()
                except UserSettings.DoesNotExist:
                    pass
                
                # Delete the user
                user.delete()
                messages.success(request, 'Account deleted successfully.')
                return redirect('accounts:login')
            else:
                messages.error(request, 'Incorrect password.')
    else:
        form = DeleteAccountForm()
    
    return render(request, 'settingsapp/delete_account.html', {'form': form})

@login_required
def reset_settings(request):
    if request.method == 'POST':
        try:
            user_settings = UserSettings.objects.get(user=request.user)
            user_settings.default_week_start = 'monday'
            user_settings.save()
            messages.success(request, 'Settings reset to default values!')
        except UserSettings.DoesNotExist:
            pass
        return redirect('settingsapp:settings_view')
    
    return render(request, 'settingsapp/reset_settings.html')

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
