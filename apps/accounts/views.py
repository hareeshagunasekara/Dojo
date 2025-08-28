from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, logout
from .forms import SignUpForm, StudentProfileForm
from .models import StudentProfile

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully! Welcome to Dojo!')
            return redirect('dashboard:home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})



@login_required
def edit_profile(request):
    # Get or create StudentProfile
    student_profile, created = StudentProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = StudentProfileForm(request.POST, request.FILES, instance=student_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('dashboard:home')
        else:
            # If form is invalid, return to the same page with errors
            return redirect('dashboard:home')
    
    # GET request - redirect to home since we handle editing via modal
    return redirect('dashboard:home')

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('accounts:login')
