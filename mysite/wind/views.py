from django.shortcuts import render
from django.shortcuts import render,render_to_response
from django.template import RequestContext   
from django.contrib.auth.models import User
from django.contrib import auth
from wind.models import UserProfile
from django.core.context_processors import csrf  
from file import excel_table
# Create your views here.
'''
index
'''
def  index(request):
    context={"js":"hello baby"}
    return render_to_response('wind/index.html',context,context_instance=RequestContext(request) )
'''
login 
'''
def  login(request):
    username = request.POST['username']
    password = request.POST['password']
    user=auth.authenticate(username=username,password=password)
    if user is not None:
        if user.is_active:
        	auth.login(request,user)
        	context={'result':'login success!'}
    else:
        context={'result':'login failed!'}
    return render_to_response('wind/index.html',context,context_instance=RequestContext(request) )



def  portal(request):
    username=request.session.get('username','anybody')
    return render_to_response('portal.html',{'username':username}) 
def echart(request):
    list1=excel_table()
    print list1
    return render_to_response('echart.html',{'list1':list1}) 

