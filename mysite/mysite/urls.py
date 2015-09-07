from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^img/(?P<path>.*)', 'django.views.static.serve', {'document_root': '/E/dwen/model/output/original'}),  
    url(r'^wind/', include('wind.urls'),name='wind'),
    url(r'^admin/', include(admin.site.urls),name='admin'),
)