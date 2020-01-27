from django import forms
from django.forms import ModelForm
from . models import *

class Category(forms.ModelForm):

    class Meta:
        model = category
        fields = [
            'name',
            'image',
        ]
class prodForm(forms.ModelForm):
    class Meta:
        model = prod
        fields = '__all__'
        # invent = category.objects.all()
        # catogeryy=forms.ModelMultipleChoiceField(queryset = invent) 
        

        widgets={
            "pname": forms.TextInput(attrs={'class':'form-control'}) 
        }
