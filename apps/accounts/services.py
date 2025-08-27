"""
Services for the accounts app.
Contains business logic for user operations.
"""

import uuid
from django.contrib.auth.models import User
from .models import StudentProfile


def create_student_profile(user: User) -> StudentProfile:
    """
    Create a student profile for a new user.
    
    Args:
        user: The user instance
        
    Returns:
        StudentProfile: The created student profile
    """
    student_id = f"STU{str(uuid.uuid4())[:8].upper()}"
    return StudentProfile.objects.create(user=user, student_id=student_id)


def update_student_profile(user: User, **kwargs) -> StudentProfile:
    """
    Update a student profile.
    
    Args:
        user: The user instance
        **kwargs: Fields to update
        
    Returns:
        StudentProfile: The updated student profile
    """
    profile = user.studentprofile
    for field, value in kwargs.items():
        if hasattr(profile, field):
            setattr(profile, field, value)
    profile.save()
    return profile


def get_student_by_id(student_id: str) -> StudentProfile:
    """
    Get a student profile by student ID.
    
    Args:
        student_id: The student ID
        
    Returns:
        StudentProfile: The student profile or None
    """
    try:
        return StudentProfile.objects.get(student_id=student_id)
    except StudentProfile.DoesNotExist:
        return None
