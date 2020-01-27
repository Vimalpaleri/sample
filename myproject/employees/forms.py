from django import forms
from . models import users

class Login(forms.Form):
    email = forms.EmailField(
        max_length = 50,
        widget= forms.TextInput(attrs= {'class':'form-control'})
    )
    password = forms.CharField(
        max_length = 20,
        min_length= 8,
        widget= forms.PasswordInput(attrs= {'class':'form-control'})
    )   
    
    def clean_email(self):
        email=self.cleaned_data.get('email')
        if(email.__contains__(' ')):
            raise forms.ValidationError("Invalid email")
        return email