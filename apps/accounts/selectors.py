"""
Selectors for the accounts app.
Contains data retrieval logic.
"""

from django.contrib.auth.models import User
from .models import StudentProfile


def get_user_profile(user: User) -> StudentProfile:
    """
    Get the student profile for a user.
    
    Args:
        user: The user instance
        
    Returns:
        StudentProfile: The student profile
    """
    return user.studentprofile


def get_all_students():
    """
    Get all student profiles.
    
    Returns:
        QuerySet: All student profiles
    """
    return StudentProfile.objects.select_related('user').all()


def get_students_by_year(year: int):
    """
    Get students by year.
    
    Args:
        year: The year to filter by
        
    Returns:
        QuerySet: Student profiles for the given year
    """
    return StudentProfile.objects.filter(
        user__date_joined__year=year
    ).select_related('user')


def search_students(query: str):
    """
    Search students by name or student ID.
    
    Args:
        query: The search query
        
    Returns:
        QuerySet: Matching student profiles
    """
    return StudentProfile.objects.filter(
        user__first_name__icontains=query
    ) | StudentProfile.objects.filter(
        user__last_name__icontains=query
    ) | StudentProfile.objects.filter(
        student_id__icontains=query
    ).select_related('user')
