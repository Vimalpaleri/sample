from django import forms
from django.forms import ModelForm,ValidationError
from . models import *
class MNewProductForm(ModelForm):
    class Meta:
        model = products
        fields = ['name','brand','quantity','price']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'brand':forms.Select(attrs={'class':'form-control'}),
            'quantity':forms.NumberInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
        }
class NewProductForm(forms.Form):
    BRANDS=(
        ('apple','apple inc'),
        ('microsoft','microsoft inc'),
        ('google','google inc'),
    )
    
    name=forms.CharField(max_length=50,min_length=5,strip=True,required=True)
    brand=forms.ChoiceField(widget=forms.Select,choices=BRANDS)
    quantity=forms.IntegerField(required=True)
    price=forms.CharField(max_length=10)

    def clean_quantity(self):
        val = int(self.cleaned_data['quantity'])
        if val <= 0:
            raise ValidationError("Please enter valid number")
        else:
            return self.cleaned_data['quantity']

