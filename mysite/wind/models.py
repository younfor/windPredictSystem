from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    phone = models.CharField(max_length=30)
    company=models.CharField(max_length=100)
    alipay=models.CharField(max_length=50)
    bank=models.CharField(max_length=50)
    level=models.CharField(max_length=10)

class  Factories(models.Model):
    name=models.CharField(max_length=30)	
    province=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    email=models.EmailField()
    def __unicode__(self):
        return self.name

class  PowerStations(models.Model):
    name=models.CharField(max_length=30)
    longitude=models.CharField(max_length=12)
    latitude=models.CharField(max_length=12)
    factory=models.ForeignKey(Factories)
    def __unicode__(self):
        return self.name             