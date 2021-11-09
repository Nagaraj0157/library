from .models import Admin,Book
from django import forms
class admin_loginform(forms.Form):
    Email=forms.CharField()
    password=forms.CharField(max_length=10)
    widgets={
    'Email':forms.EmailInput(attrs={'class':'form-control'}),
    'password':forms.PasswordInput(attrs={'class':'form-control'})

    }
  
class admin_signupform(forms.Form):
        name=forms.CharField(max_length=20)
        Email=forms.CharField()
        password=forms.CharField(max_length=10)
        reenter_password=forms.CharField(max_length=10)
        widgets={
        'name':forms.TextInput(attrs={'class':'form-control'}),
        'Email':forms.EmailInput(attrs={'class':'form-control'}),
        'password':forms.PasswordInput(attrs={'class':'form-control'}),
        'reenter_password':forms.PasswordInput(attrs={'class':'form-control'})
        }
class Book_detailform(forms.Form):
    Book_Name=forms.CharField(max_length=50)
    isbn=forms.CharField(max_length=30)
    Author=forms.CharField(max_length=30)
    Language=forms.CharField(max_length=20)
class updateform(forms.ModelForm):
    class Meta:
        model=Book
        fields='__all__'

   