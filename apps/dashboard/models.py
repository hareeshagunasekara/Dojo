from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(blank=True, null=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    custom_label = models.CharField(max_length=50, blank=True, null=True)
    course = models.ForeignKey('courses.Course', on_delete=models.SET_NULL, blank=True, null=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
