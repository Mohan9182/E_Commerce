from django import forms
from .models import User

class Signupform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','password','address','mobile']
        widgets = {
            'name' : forms.TextInput(attrs={'class':"form-control",'name':"name",'placeholder':"Name"}),
            'email' : forms.EmailInput(attrs={'class':"form-control",'name':"email",'placeholder':"Email"}),
            'password' : forms.TextInput(attrs={'class':"form-control",'name':"password",'placeholder':"Password",'type':"password"}),
            'address' : forms.Textarea(attrs={'class':"form-control",'name':"address",'placeholder':"Address"}),
            'mobile' : forms.TextInput(attrs={'class':"form-control",'name':"mobile",'placeholder':"Mobile"}),
        }
