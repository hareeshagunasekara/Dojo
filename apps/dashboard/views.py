from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Todo
from .forms import TodoForm

@login_required
def home(request):
    todos = Todo.objects.filter(user=request.user)
    form = TodoForm()
    
    context = {
        'todos': todos,
        'form': form,
        'completed_todos': todos.filter(completed=True).count(),
        'total_todos': todos.count(),
    }
    return render(request, 'dashboard/home.html', context)

@login_required
def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            messages.success(request, 'Todo added successfully!')
            return redirect('dashboard:home')
    return redirect('dashboard:home')

@login_required
def toggle_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    todo.completed = not todo.completed
    todo.save()
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'completed': todo.completed})
    
    return redirect('dashboard:home')

@login_required
def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    todo.delete()
    messages.success(request, 'Todo deleted successfully!')
    return redirect('dashboard:home')

@login_required
def edit_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Todo updated successfully!')
            return redirect('dashboard:home')
    else:
        form = TodoForm(instance=todo)
    
    return render(request, 'dashboard/edit_todo.html', {'form': form, 'todo': todo})
