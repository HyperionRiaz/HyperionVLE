from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^moocadmin/', include('moocadmin.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    
    #url(r'^accounts/loggedin/$', 'moocadmin.views.loggedin'),
    #url(r'^accounts/invalid/$',  'moocadmin.views.invalid_login'),
    
)
