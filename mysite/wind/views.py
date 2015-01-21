from django.shortcuts import render,render_to_response,HttpResponseRedirect

from django.template import RequestContext   
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from wind.models import UserProfile
from django.core.context_processors import csrf  
from excel import excel_table
from netcdf import netcdf as nc
# Create your views here.

def index(request):
    context={"js":"hello baby"}
    return render_to_response('wind/index.html',context,context_instance=RequestContext(request) )

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
                if user.is_active:
                        auth.login(request,user)
                        context={'result':'login success!','username':username}
                        print 'login success'
        else:
                context={'result':'login failed!'}
        return HttpResponseRedirect('/wind/portal')
        # return render_to_response('wind/portal.html',context)
    return render_to_response('wind/login.html',{},context_instance=RequestContext(request))

def portal(request):
    user=request.user   
    print user
    print 'user where'
    return render_to_response('wind/portal.html',{'username':user.username}) 

def echart(request):
    excel=excel_table('weather.xls',u'sheet1')
    list1=excel.get_list1()
    list2=excel.get_list2()

    print list1[0]
    return render_to_response('wind/echart.html',{'list1':list1,'list2':list2}) 

def chartout(request):
   
    root, is_new = nc.open('temper.nc')
    print root.files
    temper=nc.getvar(root, 'temperature')[0]
    week= nc.getvar(root, 'week')[0]
    print "temperature: ", temper
    print "Matrix shape: ", week
   #print "Matrix values: ", data[:]
    return render_to_response('wind/chartout.html',{'week':week,'temper':temper}) 

def signup(request):
    if request.method == 'POST': 
        username = request.POST.get('username')
        password = request.POST.get('password')
        email=request.POST.get('email')
        print username,password
        user=User.objects.create_user(username,email,password)
        user.is_staff=True
        user.save()
        print "%s,%s,%d"  % (user.username,user.password,user.is_staff)
        #if form.is_valid(): 
          #  f=form.cleaned_data
            #info=f['username']
            #print info
        return HttpResponse('sucessful signup') 
    return render(request,'wind/signup.html')
