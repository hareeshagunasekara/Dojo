from django import forms
from .models import ClassSchedule, ScheduleSlot
from apps.courses.models import Course

class ClassScheduleForm(forms.ModelForm):
    class Meta:
        model = ClassSchedule
        fields = ['title', 'instructor', 'room_location', 'color', 'course']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter schedule title'}),
            'instructor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter instructor name'}),
            'room_location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter room location'}),
            'color': forms.Select(attrs={'class': 'form-select'}),
            'course': forms.Select(attrs={'class': 'form-select'}),
        }
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['course'].queryset = Course.objects.filter(user=user)
            self.fields['course'].empty_label = "Select a course (optional)"
        
        # Set default color if not provided
        if not self.data and not self.instance.pk:
            self.fields['color'].initial = '#B7B1F2'

class ScheduleSlotForm(forms.ModelForm):
    class Meta:
        model = ScheduleSlot
        fields = ['day_of_week', 'start_time', 'end_time']
        widgets = {
            'day_of_week': forms.Select(attrs={'class': 'form-select'}),
            'start_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }

class ScheduleSlotFormSet(forms.BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.queryset = ScheduleSlot.objects.none()

ScheduleSlotFormSet = forms.modelformset_factory(
    ScheduleSlot,
    form=ScheduleSlotForm,
    formset=ScheduleSlotFormSet,
    extra=1,
    can_delete=True
)
