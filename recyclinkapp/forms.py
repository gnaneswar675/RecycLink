from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, MerchantProfile

class LoginForm(forms.Form):
    """Form for user login with user type selection"""
    
    USER_TYPES = [
        ('user', 'Individual User'),
        ('merchant', 'Business/Merchant')
    ]

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email',
            'id': 'email'
        })
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password',
            'id': 'password'
        })
    )
    
    user_type = forms.ChoiceField(
        choices=USER_TYPES,
        widget=forms.RadioSelect(attrs={
            'class': 'form-check-input'
        }),
        initial='user',
        label='Login as'
    )
    
    remember_me = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input',
            'id': 'remember-me'
        }),
        label='Remember me'
    )

    def clean_email(self):
        """Validate email exists in database"""
        email = self.cleaned_data.get('email')
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("No account found with this email")
        return email

class SignUpForm(UserCreationForm):
    USER_TYPES = [
        ('user', 'Regular User'),
        ('business', 'Business User'),
    ]
    
    email = forms.EmailField(required=True)
    full_name = forms.CharField(max_length=100)
    user_type = forms.ChoiceField(choices=USER_TYPES)
    
    # Business-specific fields (optional)
    business_name = forms.CharField(max_length=100, required=False)
    business_type = forms.ChoiceField(choices=MerchantProfile.BUSINESS_TYPES, required=False)
    address = forms.CharField(widget=forms.Textarea, required=False)
    phone = forms.CharField(max_length=15, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'full_name', 'password1', 'password2', 'user_type']

