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

# Create your views here.


def index(request):
    context = {"js": "hello baby"}
    return render_to_response('wind/index.html', context, context_instance=RequestContext(request))


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                context = {'result': 'login success!', 'username': username}
                print 'login success'
        else:
            context = {'result': 'login failed!'}
        return HttpResponseRedirect('/wind/portal')
        # return render_to_response('wind/portal.html',context)
    return render_to_response('wind/login.html', {}, context_instance=RequestContext(request))


def portal(request):
    user = auth.get_user(request)
    print user
    print 'user where'
    DBhelper.getIns().getScope(request)
    return render_to_response('wind/portal.html', {'username': user.username})


def speed(request):
    list1 = []
    list2 = []
    excel = excel_table('wind/excel_file/speed.xls', u'sheet1')
    list1 = excel.get_list1
    list2 = excel.get_list2

    print list1
    print list2
    return render_to_response('wind/speed.html', {'list1': list1, 'list2': list2})


def power(request):
    list1 = []
    list2 = []
    excel = excel_table('wind/excel_file/power.xls', u'sheet1')
    list1 = excel.get_list1
    list2 = excel.get_list2
    print list1
    print list2
    return render_to_response('wind/power.html', {'list1': list1, 'list2': list2})


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
