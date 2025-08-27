from django.urls import path
from . import views

app_name = 'schedule'

urlpatterns = [
    path('', views.schedule_view, name='schedule_view'),
    path('class/add/', views.add_class, name='add_class'),
    path('class/<int:class_id>/edit/', views.edit_class, name='edit_class'),
    path('class/<int:class_id>/delete/', views.delete_class, name='delete_class'),
]
