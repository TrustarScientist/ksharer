# accounts/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import CustomUser

# Custom user creation form
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'password1', 'password2')
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is already in use.")
        return email
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if CustomUser.objects.filter(phone=phone).exists():
            raise forms.ValidationError("Phone number is already in use.")
        return phone

# login form to handle username, email, or phone number
class CustomLoginForm(forms.Form):
    identifier = forms.CharField(
        label="Username / Email / Phone",
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your username, email, or phone number'})
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'})
    )
