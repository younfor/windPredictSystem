from django.conf.urls import patterns, include, url
from django.contrib import admin
from wind.views import PortalView
urlpatterns = patterns('wind.views',
                       url(r'^login/', 'login', name='login'),
                       url(r'^signup/', 'signup', name='signup'),
                       url(r'^index/', 'index', name='index'),
                       url(r'^portal/', PortalView.as_view(), name='portal'),
                       url(r'^speed', 'speed', name='speed'),
                       url(r'^power', 'power', name='power'),
                       url(r'^uploadfiles', 'uploadfiles', name='uploadfiles'),
                       )
