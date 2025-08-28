from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from .models import UserSettings

class UserPreferencesForm(forms.Form):
    event_reminders = forms.BooleanField(required=False, initial=True)
    course_updates = forms.BooleanField(required=False, initial=True)

class NotificationSettingsForm(forms.Form):
    event_reminders = forms.BooleanField(required=False, initial=True)
    course_updates = forms.BooleanField(required=False, initial=True)

class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = UserSettings
        fields = ['default_week_start']
        widgets = {
            'default_week_start': forms.Select(attrs={
                'class': 'form-select'
            })
        }

class DeleteAccountForm(forms.Form):
    confirm_delete = forms.BooleanField(
        required=True,
        label="I understand that this action cannot be undone",
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password to confirm'
        }),
        label="Password"
    )
