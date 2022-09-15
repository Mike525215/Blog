from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from blog.models import *
class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Username'}), label='')
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), label='')
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}), label='')
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Username'}), label='')
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), label='')
    class Meta:
        model = User
        fields = ['username', 'password']

class CreatePersonalBlogForm(forms.ModelForm):
    title = forms.CharField(max_length=100, widget=forms.Textarea(attrs={'placeholder': 'Title', 'rows': 1, 'cols': 30}), label='')
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Content', 'rows': 5, 'cols': 30}), label='')
    blog_photo = forms.ImageField(label='')
    class Meta:
        model = Blog
        fields = ['title', 'content', 'blog_photo']
