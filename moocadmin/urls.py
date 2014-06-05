from django.conf.urls import patterns, url

from moocadmin import views

urlpatterns = patterns('',
    url(r'^$',views.index,name='index'),
    url(r'^contact/$',views.contact,name='contact'),
    url(r'^signup/$',views.student_signup,name='signup'),
    url(r'^login/$', views.login),
    url(r'^auth/$',views.auth_view),
    url(r'^logout/$',views.logout),
    url(r'^setup/$',views.setup),	 #Added by Riaz
    url(r'^submit/task/$',views.upload_task,name='task')


    
)
