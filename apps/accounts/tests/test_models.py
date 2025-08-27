"""
Tests for the accounts models.
"""

from django.test import TestCase
from django.contrib.auth.models import User
from apps.accounts.models import StudentProfile


class StudentProfileModelTest(TestCase):
    """Test cases for the StudentProfile model."""
    
    def setUp(self):
        """Set up test data."""
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
    
    def test_student_profile_creation(self):
        """Test that a student profile is created automatically."""
        self.assertTrue(hasattr(self.user, 'studentprofile'))
        self.assertIsNotNone(self.user.studentprofile.student_id)
        self.assertTrue(self.user.studentprofile.student_id.startswith('STU'))
    
    def test_student_profile_str(self):
        """Test the string representation of StudentProfile."""
        expected = f"{self.user.username} - {self.user.studentprofile.student_id}"
        self.assertEqual(str(self.user.studentprofile), expected)
    
    def test_student_id_uniqueness(self):
        """Test that student IDs are unique."""
        user2 = User.objects.create_user(
            username='testuser2',
            email='test2@example.com',
            password='testpass123'
        )
        self.assertNotEqual(
            self.user.studentprofile.student_id,
            user2.studentprofile.student_id
        )
