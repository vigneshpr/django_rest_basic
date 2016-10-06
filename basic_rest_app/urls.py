from django.conf.urls import url
from basic_rest_app import views	

urlpatterns = [
    url(r'^lst/$', views.student_list),
    url(r'^det/(?P<pk>[0-9]+)/$', views.student_detail),
]