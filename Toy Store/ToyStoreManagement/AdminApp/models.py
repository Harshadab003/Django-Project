from django.db import models
from datetime import datetime
# Create your models here.
class Category(models.Model):
    cat_name = models.CharField(max_length=30)

    class Meta:
        db_table = "Category"

    def __str__(self):
        return self.cat_name

class Toy(models.Model):
    toy_name = models.CharField(max_length=30)
    price = models.FloatField(default=500)
    description = models.CharField(max_length=200)
    image = models.ImageField(default='abc.jpg',upload_to ='Images')
    cat_fk = models.ForeignKey('Category',on_delete=models.CASCADE)

    class Meta:
        db_table = "Toy"

class Accounts(models.Model):
    cardno = models.CharField(max_length=4)
    cvv = models.CharField(max_length=4)
    expiry = models.CharField(max_length=10)
    balance = models.FloatField(default=20000)

    class Meta:
        db_table = "Accounts"
    
class OrderMaster(models.Model):
    user = models.ForeignKey("UserApp.UserInfo",on_delete = models.CASCADE)
    date_of_purchase = models.DateField(default = datetime.now())
    amount = models.FloatField(default = 2000)
    details = models.CharField(max_length = 200)

    class Meta:
        db_table = "OrderMaster"