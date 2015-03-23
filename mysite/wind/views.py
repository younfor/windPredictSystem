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
# Create your views here.
from django.views.generic import TemplateView


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
    user = request.user
    list1 = []
    list2 = []
    if_post=0
    context={}
    list3=['WindTurbine1','WindTurbine2','WindTurbine3','WindTurbine4','WindTurbine5',
    'WindTurbine6','WindTurbine7','WindTurbine8','WindTurbine9']
    if request.method == 'POST':
        file_date = request.POST.get('date')
        anim = request.POST.get('anim')
        a=file_date.split('/')
        file_name=a[2]+a[0]+a[1]
        # print a[0]
        # print a[1]
        # print a[2]
        # print a[0]
        file_path='wind/excel_file/'+'Speed'+anim+file_name+".xls"
        # file_path='wind/excel_file/'+anim
        if os.path.exists(file_path):
            excel = excel_table(file_path, u'sheet1')
            list1 = excel.get_list1
            list2 = excel.get_list2
            print file_date
            print anim
            if_post=1
            context={"if_post":if_post,'list1': list1, 'list2': list2,'list3':list3,'anim':anim,
            'file_date':file_date,'username':user.username}
            return render_to_response('wind/power.html', context)
        else:
            if_notexist=1
            context={"if_post":if_post,'if_notexist':if_notexist,'list3':list3,'anim':anim,
            'file_date':file_date,'username':user.username}
            return render_to_response('wind/speed.html', context)
    else:              
        print list1
        print list2
        return render_to_response('wind/speed.html', {'list3':list3})

def power(request):
    user = request.user
    list1 = []
    list2 = []
    if_post=0
    context={}
    list3=['WindTurbine1','WindTurbine2','WindTurbine3','WindTurbine4','WindTurbine5',
    'WindTurbine6','WindTurbine7','WindTurbine8','WindTurbine9']
    if request.method == 'POST':
        file_date = request.POST.get('date')
        anim = request.POST.get('anim')
        a=file_date.split('/')
        file_name=a[2]+a[0]+a[1]
        # print a[0]
        # print a[1]
        # print a[2]
        # print a[0]
        file_path='wind/excel_file/'+'Power'+anim+file_name+".xls"
        # file_path='wind/excel_file/'+anim
        if os.path.exists(file_path):
            excel = excel_table(file_path, u'sheet1')
            list1 = excel.get_list1
            list2 = excel.get_list2
            print file_date
            print anim
            if_post=1
            context={"if_post":if_post,'list1': list1, 'list2': list2,'list3':list3,'anim':anim,
            'file_date':file_date,'username':user.username}
            return render_to_response('wind/power.html', context)
        else:
            if_notexist=1
            context={"if_post":if_post,'if_notexist':if_notexist,'list3':list3,'anim':anim,
            'file_date':file_date,'username':user.username}
            return render_to_response('wind/power.html', context)
    else:              
        print list1
        print list2
        return render_to_response('wind/power.html', {'list3':list3})
    # list1 = []
    # list2 = []
    # excel = excel_table('wind/excel_file/power.xls', u'sheet1')
    # list1 = excel.get_list1
    # list2 = excel.get_list2
    # print list1
    # print list2
    # return render_to_response('wind/power.html', {'list1': list1, 'list2': list2})



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
        # if form.is_valid():
        #  f=form.cleaned_data
        # info=f['username']
        # print info
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
            # print files.name
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
