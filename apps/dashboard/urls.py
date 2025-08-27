from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.home, name='home'),
    path('todo/add/', views.add_todo, name='add_todo'),
    path('todo/<int:todo_id>/toggle/', views.toggle_todo, name='toggle_todo'),
    path('todo/<int:todo_id>/delete/', views.delete_todo, name='delete_todo'),
    path('todo/<int:todo_id>/edit/', views.edit_todo, name='edit_todo'),
]
