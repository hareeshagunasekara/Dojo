from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from datetime import date
from .models import Course, CourseFile, CourseLink, CourseTodo
from .forms import CourseForm, CourseFileForm, CourseLinkForm, CourseTodoForm
from apps.dashboard.models import Todo

@login_required
def course_list(request):
    courses = Course.objects.filter(user=request.user)
    # Get user's courses for the add todo modal
    user_courses = Course.objects.filter(user=request.user).order_by('name')
    
    context = {
        'courses': courses,
        'user_courses': user_courses,
    }
    return render(request, 'courses/course_list.html', context)

@login_required
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.user = request.user
            course.save()
            messages.success(request, 'Course added successfully!')
            return redirect('courses:course_list')
    else:
        form = CourseForm()
    
    return render(request, 'courses/add_course.html', {'form': form})



@login_required
def course_detail_modal(request, course_id):
    course = get_object_or_404(Course, id=course_id, user=request.user)
    
    # Get todos for this specific course
    todos = Todo.objects.filter(user=request.user, course=course)
    
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
    
    context = {
        'course': course,
        'course_todos': todos,
        'current_filter': filter_type,
    }
    return render(request, 'courses/course_detail_modal.html', context)



@login_required
def upload_course_image(request, course_id):
    if request.method == 'POST' and request.FILES.get('image'):
        course = get_object_or_404(Course, id=course_id, user=request.user)
        
        # Handle the image upload
        image_file = request.FILES['image']
        
        # Update the course with the new image
        course.image = image_file
        course.save()
        
        return JsonResponse({
            'success': True,
            'image_url': course.image.url
        })
    
    return JsonResponse({'success': False, 'error': 'No image provided'})

@login_required
def edit_course(request, course_id):
    course = get_object_or_404(Course, id=course_id, user=request.user)
    
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            
            # Check if this is an AJAX request
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'message': 'Course updated successfully!'
                })
            else:
                messages.success(request, 'Course updated successfully!')
                return redirect('courses:course_list')
        else:
            # If form is invalid and it's an AJAX request
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': False,
                    'errors': form.errors
                })
            else:
                # If form is invalid, return to the edit page with errors
                return render(request, 'courses/edit_course.html', {'form': form, 'course': course})
    else:
        form = CourseForm(instance=course)
    
    return render(request, 'courses/edit_course.html', {'form': form, 'course': course})

@login_required
def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id, user=request.user)
    course.delete()
    messages.success(request, 'Course deleted successfully!')
    return redirect('courses:course_list')

@login_required
def course_files(request, course_id):
    course = get_object_or_404(Course, id=course_id, user=request.user)
    files = course.files.all()
    return render(request, 'courses/course_files.html', {'course': course, 'files': files})

@login_required
def add_file(request, course_id):
    course = get_object_or_404(Course, id=course_id, user=request.user)
    
    if request.method == 'POST':
        form = CourseFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_obj = form.save(commit=False)
            file_obj.course = course
            file_obj.save()
            
            # Check if this is an AJAX request
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'message': 'File uploaded successfully!'
                })
            else:
                messages.success(request, 'File uploaded successfully!')
                return redirect('courses:course_files', course_id=course.id)
        else:
            # If form is invalid and it's an AJAX request
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': False,
                    'errors': form.errors
                })
            else:
                # If form is invalid, return to the add file page with errors
                return render(request, 'courses/add_file.html', {'form': form, 'course': course})
    else:
        form = CourseFileForm()
    
    return render(request, 'courses/add_file.html', {'form': form, 'course': course})

@login_required
def course_links(request, course_id):
    course = get_object_or_404(Course, id=course_id, user=request.user)
    links = course.links.all()
    return render(request, 'courses/course_links.html', {'course': course, 'links': links})

@login_required
def add_link(request, course_id):
    course = get_object_or_404(Course, id=course_id, user=request.user)
    
    if request.method == 'POST':
        form = CourseLinkForm(request.POST)
        if form.is_valid():
            link = form.save(commit=False)
            link.course = course
            link.save()
            
            # Check if this is an AJAX request
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'message': 'Link added successfully!'
                })
            else:
                messages.success(request, 'Link added successfully!')
                return redirect('courses:course_links', course_id=course.id)
        else:
            # If form is invalid and it's an AJAX request
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': False,
                    'errors': form.errors
                })
            else:
                # If form is invalid, return to the add link page with errors
                return render(request, 'courses/add_link.html', {'form': form, 'course': course})
    else:
        form = CourseLinkForm()
    
    return render(request, 'courses/add_link.html', {'form': form, 'course': course})

@login_required
def course_todos(request, course_id):
    course = get_object_or_404(Course, id=course_id, user=request.user)
    todos = course.todos.all()
    return render(request, 'courses/course_todos.html', {'course': course, 'todos': todos})

@login_required
def add_course_todo(request, course_id):
    course = get_object_or_404(Course, id=course_id, user=request.user)
    
    if request.method == 'POST':
        form = CourseTodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.course = course
            todo.save()
            messages.success(request, 'Todo added successfully!')
            return redirect('courses:course_todos', course_id=course.id)
    else:
        form = CourseTodoForm()
    
    return render(request, 'courses/add_course_todo.html', {'form': form, 'course': course})
