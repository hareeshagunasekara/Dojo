from django import forms
from .models import ClassSchedule

class ClassScheduleForm(forms.ModelForm):
    class Meta:
        model = ClassSchedule
        fields = ['course', 'day_of_week', 'start_time', 'end_time', 'room', 'instructor']
        widgets = {
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
            'day_of_week': forms.Select(choices=ClassSchedule.DAY_CHOICES),
        }
