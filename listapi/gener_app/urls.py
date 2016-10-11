from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^po$', views.demo,name="post"),
    url(r'^ge/(?P<pk>[0-9]+)/$', views.listget.as_view(),name="get"),
    url(r'^up/(?P<pk>[0-9]+)/$', views.listupdate.as_view(),name="update"),
    url(r'^de/(?P<pk>[0-9]+)/$', views.listdel.as_view(),name="delete"),
		]


