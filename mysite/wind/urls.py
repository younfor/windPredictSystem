from django.conf.urls import patterns, include, url
from django.contrib import admin
from wind.views import PortalView, LoginView
urlpatterns = patterns('wind.views',
                       url(r'^login/', LoginView.as_view(), name='login'),
                       url(r'^signup/', 'signup', name='signup'),
                       url(r'^portal/', PortalView.as_view(), name='portal'),
                       url(r'^speed', 'speed', name='speed'),
                       url(r'^power', 'power', name='power'),
                       url(r'^uploadfiles', 'uploadfiles', name='uploadfiles'),
                       url(r'^weather/$', 'weather', name='weather'),
                       url(r'^seweather', 'seweather', name='seweather'),
                       url(r'^weatherDiv1/$', 'weatherDiv1', name='weatherDiv1'),
                       url(r'^weatherDiv2/$', 'weatherDiv2', name='weatherDiv2'),
                       url(r'^weatherDiv3/$', 'weatherDiv3', name='weatherDiv3'),
                       )
