from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('add/', views.add_course, name='add_course'),
    path('<int:course_id>/', views.course_list, name='course_detail'),  # Redirect to course list
    path('<int:course_id>/detail-modal/', views.course_detail_modal, name='course_detail_modal'),
    path('<int:course_id>/upload-image/', views.upload_course_image, name='upload_course_image'),
    path('<int:course_id>/edit/', views.edit_course, name='edit_course'),
    path('<int:course_id>/delete/', views.delete_course, name='delete_course'),
    path('<int:course_id>/files/', views.course_files, name='course_files'),
    path('<int:course_id>/files/add/', views.add_file, name='add_file'),
    path('<int:course_id>/links/', views.course_links, name='course_links'),
    path('<int:course_id>/links/add/', views.add_link, name='add_link'),
    path('<int:course_id>/todos/', views.course_todos, name='course_todos'),
    path('<int:course_id>/todos/add/', views.add_course_todo, name='add_course_todo'),
    path('api/courses/', views.api_courses, name='api_courses'),
]
