from django import forms
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email Address', 'class': 'form-control'}),
        required=True
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}),
        required=True,
        min_length=8,
        max_length=16,
    )

    def clean_password(self) -> str:
        password: str = self.cleaned_data.get('password') or ''

        if len(password) < 8:
            raise ValidationError('Password must be at least 8 characters long.')
        if len(password) > 16:
            raise ValidationError('Password cannot be more than 16 characters long.')

        return password
