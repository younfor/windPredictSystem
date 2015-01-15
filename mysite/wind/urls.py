from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns= patterns('wind.views',
            url(r'^login/','login',name='login'),
            url(r'^index/','index',name='index'),
            url(r'^portal/','portal',name='portal'),
            )
