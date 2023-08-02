from .models import Review
from django import forms

class ReviewForm(forms.ModelForm):
    class Meta:

        model = Review

        fields = {
            'content'

        }

        widgets = {
            'content' : forms.Textarea( attrs={
                'class' : 'form-control',
                'placeholder' : 'Write Your Review Here'
            })}