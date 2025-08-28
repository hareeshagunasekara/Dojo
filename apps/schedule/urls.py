from django.urls import path
from . import views

app_name = 'schedule'

urlpatterns = [
    path('', views.schedule_view, name='schedule_view'),
    path('add/', views.add_schedule, name='add_schedule'),
    path('<int:schedule_id>/edit/', views.edit_schedule, name='edit_schedule'),
    path('<int:schedule_id>/delete/', views.delete_schedule, name='delete_schedule'),
    path('<int:schedule_id>/add-slot/', views.add_slot_ajax, name='add_slot_ajax'),
]
