from .models import Subscriber , Contact
from django import forms


class SubscribeForm(forms.ModelForm):
    
    class Meta:
        model = Subscriber

        fields = (
            'email',        
        )

        widgets = {
                'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Email'
            })
        }

        

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'first_name',
            'last_name',
            'phone',
            'email',
            'message',
        )
        widgets = {
            'first_name' : forms.TextInput(attrs={
                'class':'form-control', 
                'placeholder':'First name'
                 
             }),
            "last_name" : forms.TextInput(attrs={
                'class':"form-control" ,
                'placeholder':"Last name"
                 
             }),
            "phone" : forms.TextInput(attrs={
                'class':"form-control" ,
                'placeholder':"Phone Number"
                 
             }),
            "email" : forms.EmailInput(attrs={
                'class':"form-control" ,
                'placeholder':"Email"
                 
             }),
            "message" : forms.TextInput(attrs={
                'class':"form-control" ,
                'placeholder':'Message'
                 
             })
             }

