from django.db import models



class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField()
    message = models.TextField()
    def __str__(self):
        return self.first_name
    

class AdvertImage(models.Model):
    advert_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='advert_images')




    def __str__(self) -> str:
        return self.advert_name
    

class Subscriber(models.Model):
    email = models.EmailField(max_length=50 , unique=True)

    def __str__(self) -> str:
        return self.email
    

class BlockedIps(models.Model):
    ip_address = models.GenericIPAddressField()