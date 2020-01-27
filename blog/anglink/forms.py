from django import forms
from django.forms import ModelForm,ValidationError
from . models import *
class MNewUserForm(ModelForm):
    class Meta:
        model = userr
        fields = ['name','age','address']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.NumberInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
        }
class NewUserForm(forms.Form):
    name=forms.CharField(max_length=50,min_length=5,strip=True,required=True)
    age=forms.IntegerField(required=True)
    address=forms.CharField(max_length=50,min_length=5,strip=True,required=True)

class NewUser(ModelForm):
    class Meta:
        model = userr
        fields = '__all__'
