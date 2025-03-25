from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import SignUpForm
from django.http import JsonResponse
from django.views.decorators.http import require_POST

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')

        # Check for user credentials
        if email == 'gnaneswar@gmail.com' and password == 'gnaneswar' and user_type == 'user':
            user = authenticate(request, username='gnaneswar', password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('user_dashboard')
            else:
                messages.error(request, 'Invalid credentials')
        
        # Check for merchant credentials
        elif email == 'gnani@gmail.com' and password == 'gnaneswar' and user_type == 'merchant':
            user = authenticate(request, username='gnani', password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('business_dashboard')
            else:
                messages.error(request, 'Invalid credentials')
        
        else:
            messages.error(request, 'Invalid email, password, or user type')
    
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



def redeem(request):
    """View function for the redeem rewards page"""
    return render(request, 'redeem.html')

def blog(request):
    return render(request, 'blog.html')

def report(request):
    return render(request, 'Report.html')

@login_required
def user_dashboard(request):
    return render(request, 'user.html')

@login_required
def business_dashboard(request):
    return render(request, 'business.html')

def feedback(request):
    return render(request, 'feedback.html')

def blog(request):
    return render(request, 'blog.html')

@require_POST
def update_points(request):
    data = json.loads(request.body)
    points = data.get('points', 0)
    
    try:
        # Update user points in your database
        user = request.user
        user.profile.points += points
        user.profile.save()
        
        return JsonResponse({
            'success': True,
            'message': f'Added {points} points successfully'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': str(e)
        }, status=400)