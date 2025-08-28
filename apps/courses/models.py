from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    COLOR_CHOICES = [
        ('#B7B1F2', 'Primary Purple'),
        ('#BFECFF', 'Secondary Blue'),
        ('#FFE0EF', 'Accent Pink'),
        ('#C1CFA1', 'Success Green'),
        ('#F0A04B', 'Warning Orange'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    instructor = models.CharField(max_length=100, blank=True)
    room_location = models.CharField(max_length=100, blank=True)
    folder_color = models.CharField(max_length=7, choices=COLOR_CHOICES, default='#B7B1F2')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at', 'name']
    
    def __str__(self):
        return self.name

class CourseFile(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='files')
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='course_files/')
    description = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class CourseLink(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='links')
    title = models.CharField(max_length=200)
    url = models.URLField()
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class CourseTodo(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='todos')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    due_date = models.DateField(blank=True, null=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
