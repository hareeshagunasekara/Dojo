from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserSettings(models.Model):
    WEEK_START_CHOICES = [
        ('monday', 'Monday'),
        ('sunday', 'Sunday'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='settings')
    default_week_start = models.CharField(
        max_length=10,
        choices=WEEK_START_CHOICES,
        default='monday'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'User Settings'
        verbose_name_plural = 'User Settings'
    
    def __str__(self):
        return f"Settings for {self.user.username}"
