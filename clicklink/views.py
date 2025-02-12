from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django import forms
from django.contrib.auth.hashers import make_password
# from .models import User
from .forms import RegistrationForm
from django.views.generic import TemplateView
from clicklink.models import User  # Ensure this is your custom user model


class RegistrationSubmittedView(TemplateView):
    template_name = "auth/registration_submitted.html"

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(email=email)  # Get user by email
            user = authenticate(request, username=user.username, password=password)  # Authenticate using username
        except User.DoesNotExist:
            user = None

        if user is not None:
            login(request, user)
            return redirect("/dashboard")  # Ensure this URL exists
        else:
            return render(request, "auth/login.html", {"error": "Invalid credentials"})

class RegisterView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/auth/registration-submitted')
        return render(request, 'register.html', {'form': form})
    
    
class ForgotPasswordView(View):
        def get(self, request):
            return render(request, 'auth/forgot_password.html')