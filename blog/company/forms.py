from django import forms
from django.forms import ModelForm,ValidationError
from . models import *
class EmployeeForm(forms.Form):
    DESIGNATION=(
        ('manager','manager com'),
        ('hr','hr com'),
        ('programmer','programmer inc'),
        ('programmer trainee','programmer_trainee com'),
        ('others','others com'),
    )
    
    name=forms.CharField(max_length=50,min_length=5,strip=True,required=True)
    designation=forms.ChoiceField(widget=forms.Select,choices=DESIGNATION)
    username=forms.CharField(required=True)
    email=forms.EmailField(max_length=30,required=True)
    password=forms.PasswordInput()

class MEmployeeForm(ModelForm):
    class Meta:
        model = employee
        fields = ['name','designation','username','email','password']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'designation':forms.Select(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
        }
class EmployeeLogin(forms.Form):
    username=forms.CharField(required=True)
    password=forms.CharField(min_length=5,required=True)
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description','document',)