from django import forms
from django.contrib.auth.models import User

class UserPreferencesForm(forms.Form):
    theme = forms.ChoiceField(
        choices=[
            ('light', 'Light'),
            ('dark', 'Dark'),
            ('auto', 'Auto'),
        ],
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    language = forms.ChoiceField(
        choices=[
            ('en', 'English'),
            ('es', 'Spanish'),
            ('fr', 'French'),
        ],
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    timezone = forms.ChoiceField(
        choices=[
            ('UTC', 'UTC'),
            ('America/New_York', 'Eastern Time'),
            ('America/Chicago', 'Central Time'),
            ('America/Denver', 'Mountain Time'),
            ('America/Los_Angeles', 'Pacific Time'),
        ],
        widget=forms.Select(attrs={'class': 'form-select'})
    )

class NotificationSettingsForm(forms.Form):
    email_notifications = forms.BooleanField(required=False, initial=True)
    todo_reminders = forms.BooleanField(required=False, initial=True)
    event_reminders = forms.BooleanField(required=False, initial=True)
    course_updates = forms.BooleanField(required=False, initial=True)
