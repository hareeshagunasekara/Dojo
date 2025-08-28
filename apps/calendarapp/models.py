from django.db import models
from django.contrib.auth.models import User
from apps.courses.models import Course

class Event(models.Model):
    EVENT_TYPE_CHOICES = [
        ('class', 'Class'),
        ('exam', 'Exam'),
        ('assignment', 'Assignment'),
        ('meeting', 'Meeting'),
        ('personal', 'Personal'),
        ('other', 'Other'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    start_time = models.TimeField(null=True, blank=True)
    end_date = models.DateField()
    end_time = models.TimeField(null=True, blank=True)
    is_all_day = models.BooleanField(default=False)
    location = models.CharField(max_length=200, blank=True)
    event_type = models.CharField(max_length=20, choices=EVENT_TYPE_CHOICES, default='other')
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True, related_name='events')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['start_date', 'start_time']
    
    def __str__(self):
        return self.title
