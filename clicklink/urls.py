from django.urls import path
from django.views.generic import TemplateView
from .views import LoginView, RegisterView, ForgotPasswordView
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('registration-submitted/', TemplateView.as_view(template_name='auth/registration_submitted.html'), name='registration.submitted'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot_password'),
    path('admin/', admin.site.urls),
]
