from django.db import models
import datetime
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    price = models.DecimalField(decimal_places=0, max_digits=10,default=0)
    description = models.CharField(max_length=500,default='', blank=True,null=True)
    picture=models.ImageField(upload_to='upload/product')

#    SIZE_CHOICES = (
#        ('m', '32'),
#        ('l', '42'),
#        ('xl', '52'),
#    )
#    size = models.CharField(max_length=4,choices=SIZE_CHOICES,default='32')
    def __str__(self):
        return f'{self.name}'

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=500,default='',blank=True)
    phone_number = models.CharField(max_length=20,blank=True,null=True)
    date = models.DateField(default=datetime.date.today)
    status = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.product}'