from django.urls import path
from . import views

app_name = 'calendarapp'

urlpatterns = [
    path('', views.calendar_view, name='calendar_view'),
    path('event/add/', views.add_event, name='add_event'),
    path('event/add/ajax/', views.add_event_ajax, name='add_event_ajax'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('event/<int:event_id>/edit/', views.edit_event, name='edit_event'),
    path('event/<int:event_id>/delete/', views.delete_event, name='delete_event'),
    path('event/<int:event_id>/delete/ajax/', views.delete_event_ajax, name='delete_event_ajax'),
    path('event/<int:event_id>/update/', views.update_event_ajax, name='update_event_ajax'),
]
