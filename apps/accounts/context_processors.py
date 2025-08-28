from .models import StudentProfile

def student_profile(request):
    """
    Add student profile to all templates if user is authenticated
    """
    if request.user.is_authenticated:
        try:
            student_profile = StudentProfile.objects.get(user=request.user)
            return {'student_profile': student_profile}
        except StudentProfile.DoesNotExist:
            # Create profile if it doesn't exist
            student_profile = StudentProfile.objects.create(user=request.user)
            return {'student_profile': student_profile}
    return {'student_profile': None}
