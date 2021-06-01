from django import forms
from .models import Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class Bookcreateform(forms.Form):
    book_name = forms.CharField(max_length=120)
    author = forms.CharField(max_length=120)
    price = forms.CharField(max_length=120)
    pages = forms.CharField(max_length=120)

    def clean(self):
        pass

class BookUpdateForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=["book_name","author","price","pages"]

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","email","username","password1","password2"]

class Loginform(forms.Form):
    username=forms.CharField(max_length=123)
    password=forms.CharField(max_length=23)