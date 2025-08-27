from django.urls import path
from . import views

app_name = 'settingsapp'

urlpatterns = [
    path('', views.settings_view, name='settings_view'),
    path('preferences/', views.preferences, name='preferences'),
    path('notifications/', views.notifications, name='notifications'),
]
