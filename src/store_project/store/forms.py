from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from store.models import UserAddress, UserVisa


# Register
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


# Login
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


# Update info
class ProfileFrom(forms.ModelForm):
    class Meta:
        model = UserAddress
        fields = ['email', 'phone', 'country', 'state', 'city', 'address']


class VisaForm(forms.ModelForm):
    class Meta:
        model = UserVisa
        fields = ['name', 'cardnumber', 'expirationdate', 'securitycode']
