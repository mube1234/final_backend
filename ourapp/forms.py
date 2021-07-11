from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from . models import *


class UserRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = MyUser
        fields = ('username','first_name','last_name','email', 'phone','school','department', 'role')

class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = MyUser
        fields = ('username','first_name','last_name','email', 'phone','school','department', 'role',)