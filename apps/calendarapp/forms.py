from django import forms
from .models import Event
from apps.courses.models import Course

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'start_date', 'start_time', 'end_date', 'end_time', 'is_all_day', 'location', 'event_type', 'course']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
            'event_type': forms.Select(choices=Event.EVENT_TYPE_CHOICES),
            'course': forms.Select(attrs={'class': 'form-select'}),
        }
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['course'].queryset = Course.objects.filter(user=user)
            self.fields['course'].empty_label = "Select a course (optional)"
