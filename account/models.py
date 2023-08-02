from django.db import models
from django.contrib.auth.models import User , AbstractUser
from django.contrib.postgres.fields import ArrayField
    

COUNTRY = [
    ('AZ' , 'Azerbaijan'),
    ('RU' , 'Russia'),
    ('TR' , 'Turkey'),
    ('UK' , 'United Kingdom')
]


class User(AbstractUser):
    email = models.EmailField(unique= True)
    phone_number = models.CharField(max_length = 20 , null=True , blank= True)
    bio = models.CharField(max_length=255 , null=True , blank= True)
    image = models.ImageField(upload_to='media/user_profile' , null=True , blank= True , default='media/images.jpeg')
    ips = ArrayField(models.GenericIPAddressField() , null= True , blank= True)


    @property
    def imageURL(self):
        try:
            url = self.image.url

        except:
            url = ''

        return url

    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'













