from django.shortcuts import render
from django.shortcuts import render,render_to_response
from django.template import RequestContext   
from django.contrib.auth.models import User
from django.contrib import auth
from wind.models import UserProfile
from django.core.context_processors import csrf  
from excel import excel_table
from netcdf import netcdf as nc
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
    excel=excel_table('weather.xls',u'sheet1')
    list1=excel.get_list1()
    list2=excel.get_list2()

    print list1[0]
    return render_to_response('echart.html',{'list1':list1,'list2':list2}) 

def chartout(request):
   
    root, is_new = nc.open('temper.nc')
    print root.files
    temper=nc.getvar(root, 'temperature')[0]
    week= nc.getvar(root, 'week')[0]
    print "temperature: ", temper
    print "Matrix shape: ", week
   #print "Matrix values: ", data[:]
    return render_to_response('chartout.html',{'week':week,'temper':temper}) 

