from django.conf.urls import patterns, url

from diamondslocation import views

urlpatterns = patterns('',
	url(r'^/addmarcador/$', views.addMarker, name='addMarker'),
	url(r'^/result/$', views.result, name='result'),
)
