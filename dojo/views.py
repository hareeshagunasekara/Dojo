from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

def welcome_view(request):
    """
    Welcome page view that redirects authenticated users to dashboard.
    """
    if request.user.is_authenticated:
        return redirect('dashboard:home')
    return render(request, 'welcome.html')

def home_redirect(request):
    """
    Redirect root URL to appropriate page based on authentication status.
    """
    if request.user.is_authenticated:
        return redirect('dashboard:home')
    return redirect('welcome')

@login_required
def dashboard_redirect(request):
    """
    Redirect authenticated users to dashboard home.
    """
    return redirect('dashboard:home')
