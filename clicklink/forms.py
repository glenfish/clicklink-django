from django import forms
from clicklink.models import User

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["email", "password"]  # No username field needed

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])  # Hash password
        user.username = user.email  # Ensure username is set to email
        if commit:
            user.save()
        return user
