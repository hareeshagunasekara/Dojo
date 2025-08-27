from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Course, CourseFile, CourseLink, CourseTodo
from .forms import CourseForm, CourseFileForm, CourseLinkForm, CourseTodoForm

@login_required
def course_list(request):
    courses = Course.objects.filter(user=request.user)
    return render(request, 'courses/course_list.html', {'courses': courses})

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
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id, user=request.user)
    return render(request, 'courses/course_detail.html', {'course': course})

@login_required
def edit_course(request, course_id):
    course = get_object_or_404(Course, id=course_id, user=request.user)
    
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course updated successfully!')
            return redirect('courses:course_detail', course_id=course.id)
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
            messages.success(request, 'File uploaded successfully!')
            return redirect('courses:course_files', course_id=course.id)
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
            messages.success(request, 'Link added successfully!')
            return redirect('courses:course_links', course_id=course.id)
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
