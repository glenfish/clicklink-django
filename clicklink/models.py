from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)  # Ensure email is unique
    username = models.CharField(max_length=150, unique=True, blank=True, null=True)  # Allow blank username
    password = models.CharField(max_length=255)
    affiliate_id = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=20, default='pending')
    deactivated = models.BooleanField(default=False)
    role = models.CharField(max_length=20, default='user')

    USERNAME_FIELD = "email"  # Use email instead of username for login
    REQUIRED_FIELDS = []  # No extra required fields

    groups = models.ManyToManyField(Group, related_name="clicklink_user_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="clicklink_user_permissions", blank=True)

    def save(self, *args, **kwargs):
        if not self.username:  # If username is empty, set it to email
            self.username = self.email
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email

class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    queue = models.CharField(max_length=255, null=True, blank=True)
    payload = models.TextField(null=True, blank=True)
    attempts = models.IntegerField(default=0)
    status = models.CharField(max_length=20, default='pending')
    zip_file = models.CharField(max_length=255, null=True, blank=True)
    reserved_at = models.DateTimeField(null=True, blank=True)
    available_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Job {self.id} - {self.status}"
