from django import forms
from .models import Checkout
from django_countries.widgets import CountrySelectWidget

class CheckoutForm(forms.ModelForm):
    
    class Meta:
        model = Checkout
        fields = (
            'address',
            'city',
            'state',
            'zipcode'


        )
    
        widgets = {                
                'address' : forms.TextInput(attrs={
                'class': "field-label",
                'placeholder' : 'Street Adress'
            }),            
                'city' : forms.TextInput(attrs={
                'class': "field-label",
            }),
                'state' : forms.TextInput(attrs={
                'class': "field-label",
            }),                    
                'zipcode' : forms.TextInput(attrs={
                'class': "field-label",
            }),        
        }   