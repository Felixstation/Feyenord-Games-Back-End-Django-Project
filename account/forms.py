from typing import Dict , Any
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm , UsernameField
User = get_user_model()


class RegisterForm(forms.ModelForm):

    class Meta:
        model = User

        fields = {
            'first_name',
            'last_name',
            'username',
            'phone_number',
            'email',
            'password',
            'image',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First Name'

            }),

                'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'

            }),
                'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last Name'

            }),
                'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Email'

            }),
                'password': forms.PasswordInput(attrs={
                'type': 'password',
                'class': 'form-control',
                'placeholder': 'Password'

            }),
                'phone_number': forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Phone'

            }),

        }


    def save(self, commit: bool = ...) -> Any:
        user = super().save(commit)
        user.set_password(self.cleaned_data['password'])
        user.is_active = False
        user.save()
        return user
    

class LoginForm(AuthenticationForm):
    username = UsernameField(max_length=40, widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email',
            }))
    password = forms.CharField(max_length=40, widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password',
            }))

    

class UserProfileUpdateForm(forms.ModelForm):
   
    class Meta:
        model =User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'bio',
            'phone_number',
            'image',
        
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
        "username" : forms.TextInput(attrs={
                    'class':"form-control" ,
                    'placeholder':"Username"
                    
                }),
        "phone_number" : forms.TextInput(attrs={
                    'class':"form-control" ,
                    'placeholder':"Phone Number"
                    
                }),
        "bio" : forms.Textarea(attrs={
                    'class':"form-control" ,
                    'placeholder':"Bio"
                    
                }),
        "email" : forms.EmailInput(attrs={
                    'class':"form-control" ,
                    'placeholder':"Email"
                    
                }),
      
    }
