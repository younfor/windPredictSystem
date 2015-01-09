from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    telephone = models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    level=models.CharField(max_length=10)
    father=models.ForeignKey('self',default=None,null=True,blank=True)
    def __unicode__(self):
       return self.user.username

class  Factory(models.Model):
    name=models.CharField(max_length=30)    
    province=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    contact=models.CharField(max_length=30)
    telephone=models.CharField(max_length=30)
    email=models.EmailField()
    user=models.ForeignKey(User,unique=True)
    bank_account=models.CharField(max_length=30)
    def __unicode__(self):
       return self.name

class  PowerStation(models.Model):
    name=models.CharField(max_length=30)
    province=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    contact=models.CharField(max_length=30)
    telephone=models.CharField(max_length=30)
    email=models.EmailField()
    user=models.ForeignKey(User,unique=True)
    bank_account=models.CharField(max_length=30)
    factory=models.ForeignKey(Factory) 
    def __unicode__(self):
       return self.name

class WindTurbine(models.Model):
    name=models.CharField(max_length=30)
    longitude=models.CharField(max_length=12)
    latitude=models.CharField(max_length=12)
    contact=models.CharField(max_length=30)
    telephone=models.CharField(max_length=30)
    email=models.EmailField()
    user=models.ForeignKey(User,unique=True)
    powerstation=models.ForeignKey(PowerStation)
    def __unicode__(self):
       return self.name
