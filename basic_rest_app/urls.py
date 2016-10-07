from django.conf.urls import url
from basic_rest_app import views	
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^list/$', views.student_list),
    url(r'^show/(?P<pk>[0-9]+)/$', views.student_detail),
]
#urlpatterns = format_suffix_patterns(urlpatterns)