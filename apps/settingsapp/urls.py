from django.urls import path
from . import views

app_name = 'settingsapp'

urlpatterns = [
    path('', views.settings_view, name='settings_view'),
    path('change-password/', views.change_password, name='change_password'),
    path('delete-account/', views.delete_account, name='delete_account'),
    path('reset-settings/', views.reset_settings, name='reset_settings'),
    path('preferences/', views.preferences, name='preferences'),
    path('notifications/', views.notifications, name='notifications'),
]
