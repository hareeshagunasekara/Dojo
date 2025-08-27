from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import StudentProfile
import uuid

@receiver(post_save, sender=User)
def create_student_profile(sender, instance, created, **kwargs):
    if created:
        # Generate a unique student ID
        student_id = f"STU{str(uuid.uuid4())[:8].upper()}"
        StudentProfile.objects.create(user=instance, student_id=student_id)

@receiver(post_save, sender=User)
def save_student_profile(sender, instance, **kwargs):
    if hasattr(instance, 'studentprofile'):
        instance.studentprofile.save()
