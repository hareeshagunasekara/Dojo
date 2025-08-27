from django.contrib import admin
from .models import StudentProfile

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'student_id', 'phone_number', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'student_id')
    readonly_fields = ('student_id', 'created_at', 'updated_at')
