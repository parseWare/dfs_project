from email.policy import default
from django.db import models



# Create your models here.

class Dfs_model(models.Model):
    name = models.CharField(max_length=250,null=False)
    roll_no = models.IntegerField(default=0,blank=False,null=False)
    # image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    image = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    contact = models.IntegerField(default=0)



class Dfs_model_new(models.Model):
    name = models.CharField(max_length=250,null=False)
    roll_no = models.IntegerField(default=0,blank=False,null=False)
    # image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    image = models.CharField(max_length=250, default='')
    city = models.CharField(max_length=250)
    contact = models.IntegerField(default=0)