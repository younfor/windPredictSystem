from django.shortcuts import render
from django.shortcuts import render,render_to_response
from django.contrib.auth.models import User
from wind.models import UserProfile
# Create your views here.
def  login(request):
    u=User(username='youy',last_name='youy')
    u.set_password('you')
    u.save()
    up=UserProfile(phone='10086',user=u)
    up.save()
    context={}
    return render_to_response('wind/index.html',context)