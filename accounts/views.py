from django.shortcuts import render

# Create your views here.
# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomLoginForm, CustomUserCreationForm
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_backends


# Registration view
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            backend = get_backends()[0]  # get your custom backend
            user.backend = f"{backend.__module__}.{backend.__class__.__name__}"
            login(request, user)  # Auto login after registration
            return redirect('newsfeed')  # Change this to your homepage
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})



# Custom login view to handle username, email, or phone number
def custom_login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            identifier = form.cleaned_data['identifier']
            password = form.cleaned_data['password']
            user = authenticate(request, username=identifier, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome, {user.username}!")
                return redirect('newsfeed')  # Replace with your landing page name
            else:
                messages.error(request, "Invalid credentials. Please try again.")
    else:
        form = CustomLoginForm()
    return render(request, 'accounts/login.html', {'form': form})


@login_required
def newsfeed_view(request):
    # Placeholder for newsfeed view logic
    return render(request, 'accounts/newsfeed.html')  # Replace with actual template

# Logout view
def logout_view(request):
    print("in log out view")
    logout(request)
    return redirect('login')
