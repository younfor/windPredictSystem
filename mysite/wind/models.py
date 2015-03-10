from django.contrib.auth.models import User
from django.db import models
from django.db.models import signals
from django import forms

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    telephone = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=50, null=True)
    level = models.CharField(max_length=10, null=True)
    father = models.ForeignKey('self', default=None, null=True, blank=True)

    def __unicode__(self):
        return self.user.username

class Location(models.Model):
    province = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    def __unicode__(self):
        return self.province,self.city,self.country

class Factory(models.Model):
    name = models.CharField(max_length=30)
    province = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    contact = models.CharField(max_length=30)
    telephone = models.CharField(max_length=30)
    email = models.EmailField()
    user = models.ForeignKey(User, unique=True)
    bank_account = models.CharField(max_length=30)
    location = models.ForeignKey(Location, unique=True,null=True)
    begintime = models.DateTimeField(null=True) 
    endtime = models.DateTimeField(null=True)
    def __unicode__(self):
        return self.name

    class Admin:
        pass


class PowerStation(models.Model):
    name = models.CharField(max_length=30)
    province = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    contact = models.CharField(max_length=30)
    telephone = models.CharField(max_length=30)
    email = models.EmailField()
    user = models.ForeignKey(User, unique=True)
    bank_account = models.CharField(max_length=30)
    factory = models.ForeignKey(Factory)
    location = models.ForeignKey(Location, unique=True,null=True)
    begintime = models.DateTimeField(null=True) 
    endtime = models.DateTimeField(null=True)
    def __unicode__(self):
        return self.name


class WindTurbine(models.Model):
    name = models.CharField(max_length=30)
    longitude = models.CharField(max_length=12)
    latitude = models.CharField(max_length=12)
    contact = models.CharField(max_length=30)
    telephone = models.CharField(max_length=30)
    email = models.EmailField()
    user = models.ForeignKey(User, unique=True)
    powerstation = models.ForeignKey(PowerStation)
    location = models.ForeignKey(Location, unique=True,null=True)
    begintime = models.DateTimeField(null=True) 
    endtime = models.DateTimeField(null=True)
    def __unicode__(self):
        return self.name



class PowerData(models.Model):
    turbine = models.ForeignKey(WindTurbine, unique=True,null=True)
    time = models.CharField(max_length=30,null=True)
    NWP_speed =models.CharField(max_length=30,null=True)
    CFD_speed =models.CharField(max_length=30,null=True)
    Observed_speed=models.CharField(max_length=30,null=True)
    Observed_power=models.CharField(max_length=30,null=True)
    Predicted_speed=models.CharField(max_length=30,null=True)
    Speed_dev=models.CharField(max_length=30,null=True)
    Predicted_power=models.CharField(max_length=30,null=True)
    Power_dev=models.CharField(max_length=30,null=True)

class UploadFileForm(forms.Form):
    file = forms.FileField()
