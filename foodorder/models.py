from django.db import models

# Create your models here.

class userinfo(models.Model):
    uname=models.CharField(max_length=30)
    uemail=models.CharField(max_length=30)
    umobile=models.CharField(max_length=15)
    upassword=models.CharField(max_length=20)
    def __str__(self):
        return self.uname


class foodmenu(models.Model):
    foodname=models.CharField(max_length=30)
    foodprice=models.IntegerField()
    foodpic=models.CharField(max_length=50)
    def __str__(self):
        return self.foodname

class orderhist(models.Model):
    uemail=models.CharField(max_length=30)
    ubillno=models.CharField(max_length=30)
    # udate=models.CharField(max_length=30)
    uamount=models.IntegerField()
    def __str__(self):
        return self.uemail

class ddcard(models.Model):
    foodname=models.CharField(max_length=30)
    foodquant=models.CharField(max_length=10)
    orderid=models.CharField(max_length=30)
    def __str__(self):
        return self.foodname

