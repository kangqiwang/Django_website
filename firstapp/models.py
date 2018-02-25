from django.db import models

# Create your models here.
class Product(models.Model):
	title=models.CharField(null=True, blank=True, max_length=300)
	image=models.ImageField(upload_to="img")
	def __str__(self):
		return self.title
"""
class ShopCart(models.Model):
	card_id=models.CharField(max_length=256)
	product=models.ForeignKey(to=Product, unique=Flase)
	quantity=models.IntegerField(default=1)
	create_time=models.DateTimeField(null=True,blank=True,default=None)
	def __str__(self):
		return self.product.title+" quantity:"+str(self.quantity)
	
	def sum_proce(self):
		return self.quantity*self.product.new_price
	
	def add_quantity(self):
		self.quantity+=1
		self.save()
	
	def del_quantity(self):
		self.quantity-=1
		if self.quantity<1:
			self.delete()
		else:
			self.save()
	def delete_product(self):
		self.delete()
"""