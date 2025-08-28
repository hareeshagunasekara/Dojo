from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from datetime import date, datetime
from .models import Todo
from .forms import TodoForm
from apps.accounts.models import StudentProfile
from apps.courses.models import Course

@login_required
def home(request):
    # Get or create StudentProfile
    student_profile, created = StudentProfile.objects.get_or_create(user=request.user)
    
    todos = Todo.objects.filter(user=request.user)
    form = TodoForm()
    
    # Get filter parameter
    filter_type = request.GET.get('filter', 'all')
    today = date.today()
    
    # Apply filters based on selection
    if filter_type == 'ongoing':
        # Ongoing: not completed and due date is today or in the future
        todos = todos.filter(
            completed=False,
            due_date__gte=today
        )
    elif filter_type == 'missed':
        # Missed: not completed and due date is in the past
        todos = todos.filter(
            completed=False,
            due_date__lt=today
        )
    elif filter_type == 'completed':
        # Completed: marked as completed
        todos = todos.filter(completed=True)
    # 'all' shows all todos (no additional filter)
    
    # Add is_missed property to each todo for template styling
    for todo in todos:
        todo.is_missed = not todo.completed and todo.due_date and todo.due_date < today
    
    # Calculate todo statistics for all todos (not filtered)
    all_todos = Todo.objects.filter(user=request.user)
    completed_todos = all_todos.filter(completed=True).count()
    total_todos = all_todos.count()
    
    # Calculate ongoing todos (not completed and due date is today or in the future)
    ongoing_todos = all_todos.filter(
        completed=False,
        due_date__gte=today
    ).count()
    
    # Calculate missed todos (not completed and due date is in the past)
    missed_todos = all_todos.filter(
        completed=False,
        due_date__lt=today
    ).count()
    
    # Calculate progress percentage
    progress_percentage = 0
    if total_todos > 0:
        progress_percentage = int((completed_todos / total_todos) * 100)
    
    # Get user's courses for the todo label dropdown
    user_courses = Course.objects.filter(user=request.user).order_by('name')
    
    context = {
        'todos': todos,
        'form': form,
        'completed_todos': completed_todos,
        'ongoing_todos': ongoing_todos,
        'missed_todos': missed_todos,
        'total_todos': total_todos,
        'progress_percentage': progress_percentage,
        'today': today,
        'current_filter': filter_type,
        'student_profile': student_profile,
        'user_courses': user_courses,
    }
    return render(request, 'dashboard/home.html', context)

@login_required
def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            
            # Handle label fields
            custom_label = request.POST.get('custom_label')
            course_id = request.POST.get('course_label')
            
            if custom_label:
                todo.custom_label = custom_label
            elif course_id:
                try:
                    todo.course = Course.objects.get(id=course_id, user=request.user)
                except Course.DoesNotExist:
                    pass
            
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
            # If form is invalid, return to the same page with errors
            return redirect('dashboard:home')
    
    # GET request - redirect to home since we handle editing via modal
    return redirect('dashboard:home')
