from django.shortcuts import render, render_to_response, HttpResponseRedirect
from django.template import RequestContext
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from wind.models import UserProfile, UploadFileForm
from wind import models
from django.core.context_processors import csrf
from excel import excel_table
from DBhelper import DBhelper
import os
import json
from txtNotAll import txtNotAll
from txttoexcel import txt_file
from csvToFile import csvToFile
from csvToFile2 import csvToFile2
from CmdExec import getDate
from CmdExec import CmdExec
from colunmTxt import colunmTxt
# Create your views here.
from django.views.generic import TemplateView
import time


class CommMixin(object):

    def get_context_data(self, **kwargs):
        context = super(CommMixin, self).get_context_data(**kwargs)
        context['username'] = '3'
        if self.request.user.is_authenticated():
            context['username'] = self.request.user
        else:
            context['username'] = 'undefined'
        return context


class PortalView(CommMixin, TemplateView):

    template_name = 'wind/portal.html'

    def get_context_data(self, **kwargs):
        context = super(PortalView, self).get_context_data(**kwargs)
        print 'user where'
        data = [[41.875330, 14.102411, "helloworld"],
                [41.85330, 14.502411, "hello"]]
        #circle = DBhelper.getIns().getScope(request)
        circle = [[41.675330, 14.102411, 4000], [41.45330, 14.502411, 5000]]
        context['data'] = data
        context['circle'] = circle
        context['level'] = 1
        return context


class LoginView(TemplateView):

    template_name = 'wind/login.html'

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                print 'login success'
                return HttpResponseRedirect('/wind/portal')
        else:
            print 'login failed'


def speed(request):
     # fileave="wind/csvFile/wind prediction_out_weight ave.csv"
     # filelow="wind/csvFile/wind prediction_out_weight ave low.csv"
     # filehigh="wind/csvFile/wind prediction_out_weight ave high.csv"
     # fileExp="wind/csvFile/T6 power.txt"
     #filesum="wind/csvFile/speed/BMMnnet_output_out-sample_t6_2013-01-03-06-30:00.csv"
     filesum="/E/dwen/chris_test/Run_Chris_codes/WATCFD_software/pyper_wind_speed_nnet/BMMnnet_output_out-sample_t6_2013-01-03-06-30:00.csv"
     # fileddd="wind/excel_file/q.txt"
     #if os.path.exists(fileave) and os.path.exists(filelow) and os.path.exists(filehigh) and os.path.exists(fileExp):
        # csv=csvToFile(fileave)
        # csv_list_ave=csv.get_list()
        # #print len(csv_list_ave)
        # list1=csv_list_ave
        # print list1[1]
        # csv=csvToFile(filelow)
        # csv_list_low=csv.get_list()
        # #print len(csv_list_low)
        # csv=csvToFile(filehigh)
        # csv_list_high=csv.get_list()
        # #print len(csv_list_high)
        # txtExp=txtNotAll(fileExp,240,384)
        # list_exp=txtExp.get_list()
        #print list_exp
        #for a in list_exp:
           # print a 
     # dd=txt.get_chartlist(5)
     # print dd
     # txtd=txt.get_chartlist(4)
     # print txtd
     # print txt_list[0]
     #print "test1"
     DBhelper.getIns().getPlotWindByHeight()
     #print "test2"
     DBhelper.getIns().getPlotWRF()
     #print "test3"
     DBhelper.getIns().getExtactWindSpeedByPoint()
     user = request.user
     if_post=0
     context={}
     list3=['WindTurbine1','WindTurbine2','WindTurbine3','WindTurbine4','WindTurbine5',
    'WindTurbine6','WindTurbine7','WindTurbine8','WindTurbine9']
     if request.method == 'POST':
       #//////////////////////xiugaiwenjian path/////////////////////////
         file_date = request.POST.get('datetimepicker')
         anim = request.POST.get('anim')
         # a=file_date.split(' ')
         # print a 
         # date=a[0].split('/')
         # time=a[1].split(':')
         # print date[0],date[1],date[2],time[0],time[1]
         # file_name=date[0]+date[1]+date[2]+time[0]
       # //////////////////////xiugaiwenjian path/////////////////////
        # print a[0]
        # print a[1]
        # print a[2]
        # print a[0]
         # txtpath="/img/extr_dm4_wsp_at_25.29D121.58D68.50M.txt"
         #file_path='wind/excel_file/'+'Power'+anim+file_name+".xls"
        # file_path='wind/excel_file/'+anim
         if os.path.exists(filesum):
            csv=csvToFile2(filesum)
            obs=csv.get_list(6)
            ave=csv.get_list(8)
            high=csv.get_list(10)
            low=csv.get_list(9)
            year=csv.get_list(0)
            month=csv.get_list(1)
            day=csv.get_list(2)
            hour=csv.get_list(3)
            minute=csv.get_list(4)
            date_time=csv.get_date(year,month,day,hour,minute)
            #print list_exp
            #for a in list_exp:
                #print a
            if_post=1
            list1=obs
            context={"if_post":if_post,'date_time':date_time,'ave': ave,'low':low,'high':high,
            "obs":obs,'list3':list3,'anim':anim,'username':user.username}
            return render_to_response('wind/speed.html', context)
         else:
            print "HHHHHHHHHHHHHHHHHH"
            if_notexist=1
            context={"if_post":if_post,'if_notexist':if_notexist,'list3':list3,'anim':anim,
            'username':user.username}
            return render_to_response('wind/speed.html', context)
     else:              
        #print list1
        #print list2
        return render_to_response('wind/speed.html', {'list3':list3})

def power(request):
     # fileave="wind/csvFile/wind prediction_out_weight ave.csv"
     # filelow="wind/csvFile/wind prediction_out_weight ave low.csv"
     # filehigh="wind/csvFile/wind prediction_out_weight ave high.csv"
     # fileExp="wind/csvFile/T6 power.txt"
     #filesum="wind/csvFile/power/BMMnnet_output_out-sample_t6_2013-01-03-06-30:00.csv"
     filesum="/E/dwen/chris_test/Run_Chris_codes/WATCFD_software/pyper_wind_power_nnet/BMMnnet_output_out-sample_t6_2013-01-03-06-30:00.csv"
     #print "test1"
     DBhelper.getIns().getPlotWindByHeight()
     #print "test2"
     DBhelper.getIns().getPlotWRF()
     #print "test3"
     DBhelper.getIns().getExtactWindSpeedByPoint()
     user = request.user
     if_post=0
     context={}
     list3=['WindTurbine1','WindTurbine2','WindTurbine3','WindTurbine4','WindTurbine5',
    'WindTurbine6','WindTurbine7','WindTurbine8','WindTurbine9']
     if request.method == 'POST':
       #//////////////////////xiugaiwenjian path/////////////////////////
         file_date = request.POST.get('datetimepicker')
         anim = request.POST.get('anim')
         
         if os.path.exists(filesum):
            csv=csvToFile2(filesum)
            obs=csv.get_list(5)
            ave=csv.get_list(8)
            high=csv.get_list(10)
            low=csv.get_list(9)
            year=csv.get_list(0)
            month=csv.get_list(1)
            day=csv.get_list(2)
            hour=csv.get_list(3)
            minute=csv.get_list(4)
            date_time=csv.get_date(year,month,day,hour,minute)

            if_post=1
            list1=obs
            context={"if_post":if_post,'date_time':date_time,'ave': ave,'low':low,'high':high,
            "obs":obs,'list3':list3,'anim':anim,'username':user.username}
            return render_to_response('wind/power.html', context)
         else:

            if_notexist=1
            context={"if_post":if_post,'if_notexist':if_notexist,'list3':list3,'anim':anim,
            'username':user.username}
            return render_to_response('wind/power.html', context)
     else:              

        return render_to_response('wind/power.html', {'list3':list3})


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        print username, password
        user = User.objects.create_user(username, email, password)
        user.is_staff = True
        user.save()
        print "%s,%s,%d" % (user.username, user.password, user.is_staff)
 
        return HttpResponse('sucessful signup')
    return render(request, 'wind/signup.html')


def uploadfiles(request):
    if_success = 0
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            files = request.FILES['file']
            fname = files.name
            suffix = fname.find('.')
            print suffix
            fstyle = fname[suffix:]      # to know if xls
            if fstyle == '.xls':

                print fname[suffix:]
                # print files.size
                fp = file('wind/upload/' + fname, 'wb')
                s = files.read()
                fp.write(s)
                fp.close()
                form = UploadFileForm()
                if_success = 1
                # add Powerdata
                pdata = models.PowerData.objects.create(
                    time='1-8', NWP_speed=files.name)
                DBhelper.getIns().addPowerData(pdata)
                return render_to_response('wind/uploadfiles.html', {
                    'form': form, 'if_success': if_success, 'filename': files.name})
            else:
                form = UploadFileForm()
                if_xls = 1
                return render_to_response('wind/uploadfiles.html', {
                    'form': form, 'if_xls': if_xls})
        else:
            if_addfile = 1
            return render_to_response('wind/uploadfiles.html', {
                'form': form, 'if_addfile': if_addfile})
            # return HttpResponse('Upload,Successful!')
    else:
        form = UploadFileForm()
    return render_to_response('wind/uploadfiles.html', {
        'form': form,
        'if_success': if_success})



def weather(request):
    list3=['WindTurbine1','WindTurbine2','WindTurbine3','WindTurbine4','WindTurbine5',
    'WindTurbine6','WindTurbine7','WindTurbine8','WindTurbine9']
    if request.method == 'POST':
        Dm = request.POST.get('domain')
        Ht = request.POST.get('Ht')
        Fr= request.POST.get('datetimepicker1')
        To = request.POST.get('datetimepicker2')

        cmd=CmdExec.getIns()
        cmd.execCmd(-1,Dm,Ht,Fr,To)

        #shengchengtupian dizhi
        imgpath=[]
        for i in range(0,18):
            img="/img/anim_wind00"
            img1 = "/img/anim_wind0"
            if i<10:
                img = img + '%d'%i + ".png"
                imgpath.append(img)    
            else:
                img1 = img1 + '%d'%i + ".png"
                imgpath.append(img1)
        print imgpath
        return render_to_response('wind/weather.html',{"img":img,"imgpath":imgpath})
        # return render(request, 'wind/weather.html')
    else:
        return render_to_response('wind/weather.html',{})
        # return render(request, 'wind/weather.html')


def seweather(request):

    list3=['WindTurbine1','WindTurbine2','WindTurbine3','WindTurbine4','WindTurbine5',
    'WindTurbine6','WindTurbine7','WindTurbine8','WindTurbine9']
    if request.method == 'POST':
        Dm = request.POST.get('Dm')
        Agh = request.POST.get('Agh')
        Ht = request.POST.get('Ht')
        Lat =  request.POST.get('Lat')
        Lon =  request.POST.get('Lon')
        time1= request.POST.get('datetimepicker1')
        time2= request.POST.get('datetimepicker2')
        
        img=1
        # print "sdfffffffffffffffffffffffffffffff"
        print Dm
        print Agh
        print Ht
        print Lat
        print Lon
        print time1
        print getDate(time1)
        print 2
        print time2


        imgpath=["/img/extract_point_wind_timeseries.ncl.png",
        "/img/extract_wind_stream_field_h.ncl.png",
        "/img/windfield2013-02-04_12:30:00_dm1-200.5m.png",
        "/img/windspeed_dm1lat25.29lon121.58h.png",
        "/img/wrf_map.ncl.png"]
        # print imgpath  
        return render_to_response('wind/weather2.html',{"img":img,"imgpath":imgpath,"list3":list3})
        # return render(request, 'wind/weather.html')
    else:
        return render_to_response('wind/weather2.html',{"list3":list3})
        # return render(request, 'wind/weather.html')

def weatherDiv1(request):
    # i = 0;
    # while (i<=100000):
    #     print i
    #     i=i+1
    print "11FFFFFFFF"
    COMMPATH = "/E/dwen/model/output/original/"
    Dm = request.GET.get('Dm')
    Ht = request.GET.get('Ht')
    Dt= request.GET.get('Dt')
    print "11DDDDDDDDD"
    cmd=CmdExec.getIns()
    cmd.execCmd(0,Dm,Ht,Dt)
    #here is imgPath , please focus on it !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #just like /E/dwen/model/output/original/china_lat-5.01lon81.43_lat33.23lon174.14-2013-feb/windfield2013-02-04_12:30:00_dm1-200.5m.png
    imgPath= "/img/"+'windfield'+getDate(Dt)+'_dm'+Dm+'-'+Ht+'m.png'
    print imgPath
    #imgPath = "/img/4.jpg"
    return HttpResponse(
        json.dumps(imgPath),
        content_type='application/json')
  


def weatherDiv2(request):
    # i = 0;
    # while (i<=100000):
    #     print i
    #     i=i+1
    COMMPATH = "/E/dwen/model/output/original/"
    Dm = request.GET.get('Dm')
    agh=68.5
    Lat = request.GET.get('Lat')
    Lon= request.GET.get('Lon')
    Agh = request.GET.get('Agh')
    St= request.GET.get('St')
    Et= request.GET.get('Et')
    print "2222DDDDDDDDD"
    latfloat=float(Lat)
    lonfloat=float(Lon)
    cmd=CmdExec.getIns()
    cmd.execCmd(1,Dm,Agh,Lat,Lon,St,Et)
    filePre = '/E/dwen/model/output/original/'    
    #filePre ='/home/shinneyou/model/output/original/2013_01_30min_gn'
    imgPath="/img/"+'windspeed_dm'+Dm+'lat'+("%.2f" % latfloat)+'lon'+("%.2f" % lonfloat)+'h68.50m'+getDate(St)+'-'+getDate(Et)+'.png'
    txtPath='windspeed_dm'+Dm+'lat'+("%.2f" % latfloat)+'lon'+("%.2f" % lonfloat)+'h68.50m'+getDate(St)+'-'+getDate(Et)+'.txt'
    print "a"
    b=filePre + txtPath
    print b
    txtResult = colunmTxt(b)
    Ydata = txtResult.getColunm(5)
    year = txtResult.getColunm(0)
    month = txtResult.getColunm(1)
    day = txtResult.getColunm(2)
    hour = txtResult.getColunm(3)
    minute = txtResult.getColunm(4)
    Xdata = txtResult.get_date(year,month,day,hour,minute)
    l = len(Ydata)
    a=[ [ ] ] * 2
    a[0]=Xdata
    a[1]=Ydata
    arrayString = map(str,a)
    print arrayString
    #b = json.dumps(a)
    #print b
    return HttpResponse(
        json.dumps(arrayString),
        content_type='application/json')

def weatherDiv3(request):
    # i = 0;
    # while (i<=100000):
    #     print i
    #     i=i+1
    COMMPATH = "/E/dwen/model/output/original/"
    print "33FFFFFF"
    Dm = request.GET.get('Dm') 
    cmd=CmdExec.getIns()
    cmd.execCmd(2,Dm)
    imgPath="/img/"+'WRF_map_dm'+Dm+'.png'
    #imgPath= "/img/extract_point_wind_timeseries.ncl.png"
    print imgPath
    return HttpResponse(
        json.dumps(imgPath),
        content_type='application/json')

   
