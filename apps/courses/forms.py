from django import forms
from .models import Course, CourseFile, CourseLink, CourseTodo

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'code', 'description', 'instructor', 'semester', 'year']
        widgets = {
            'semester': forms.Select(choices=Course.SEMESTER_CHOICES),
        }

class CourseFileForm(forms.ModelForm):
    class Meta:
        model = CourseFile
        fields = ['title', 'file', 'description']

class CourseLinkForm(forms.ModelForm):
    class Meta:
        model = CourseLink
        fields = ['title', 'url', 'description']

class CourseTodoForm(forms.ModelForm):
    class Meta:
        model = CourseTodo
        fields = ['title', 'description', 'due_date', 'priority']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'priority': forms.Select(choices=CourseTodo.PRIORITY_CHOICES),
        }
