from django import forms
from .models import User, Whelp, Adopter


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'password']


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class WhelpsForm(forms.ModelForm):
    class Meta:
        model = Whelp
        fields = ['name', 'age', 'description', 'image']


class AdopterForm(forms.ModelForm):
    class Meta:
        model = Adopter
        fields = '__all__'
