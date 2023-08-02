from django.db import models
from django_countries.fields import CountryField
from django.core.validators import MinLengthValidator
from django.contrib.auth import get_user_model
from product.models import ProductVersion , ProductImage

User = get_user_model()

    

class Order(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.user.get_full_name())
		
	@property
	def shipping(self):
		shipping = True

		return shipping

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total 

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total 


class Checkout(models.Model):
    user = models.ForeignKey(User , on_delete=models.SET_NULL , null = True)
    order = models.ForeignKey(Order , on_delete=models.SET_NULL , null =True)
    address = models.CharField(max_length=60)
    country = CountryField(null= True , blank= True)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=15)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.address


class OrderItem(models.Model):
	product = models.ForeignKey(ProductVersion, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total
	



	def __str__(self) -> str:
		return f'{self.product.product_id.name} - {self.order.user.get_full_name()}'