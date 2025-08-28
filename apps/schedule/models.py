from django.db import models
from django.contrib.auth.models import User
from apps.courses.models import Course

class ClassSchedule(models.Model):
    COLOR_CHOICES = [
        ('#B7B1F2', 'Primary Purple'),
        ('#BFECFF', 'Secondary Blue'),
        ('#FFE0EF', 'Accent Pink'),
        ('#C1CFA1', 'Success Green'),
        ('#F0A04B', 'Warning Orange'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    instructor = models.CharField(max_length=100)
    room_location = models.CharField(max_length=100)
    color = models.CharField(max_length=7, choices=COLOR_CHOICES, default='#3ED0AE')
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True, related_name='schedules')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title

class ScheduleSlot(models.Model):
    DAY_CHOICES = [
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    ]
    
    schedule = models.ForeignKey(ClassSchedule, on_delete=models.CASCADE, related_name='slots')
    day_of_week = models.CharField(max_length=10, choices=DAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order', 'start_time']
        unique_together = ['schedule', 'day_of_week', 'start_time']
    
    def __str__(self):
        return f"{self.schedule.title} - {self.get_day_of_week_display()} {self.start_time}-{self.end_time}"
