from django.shortcuts import render
from rest_framework import generics
from django.core import serializers
from gener_app.models import *
from gener_app.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
# Create your views here.

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class listget(generics.RetrieveUpdateAPIView):
	queryset = gener_api.objects.all()
	serializer_class = apiSerializer

# class listcreate(APIView): #post
@csrf_exempt
def demo(request):
	if request.method == 'POST':
		data1 = JSONParser().parse(request)
		print data1
		data={'published_year': 1978, 'publication': 'Mathi', 'author': 'Selvi', 'bookname': 'CC', 'dept': 'SE'}
		serializer = apiSerializer(data=data)
        if serializer.is_valid():
        	serializer.save()
        	#print serializer.data
        	return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)	

class listdel(generics.DestroyAPIView): #delete
	queryset = gener_api.objects.all()
	serializer_class = apiSerializer

class listupdate(generics.UpdateAPIView): #update
	queryset = gener_api.objects.all()
	serializer_class = apiSerializer

	#{'published_year': 1984, 'publication': u'radha', 'author': u'annie', 'bookname': u'EVS', 'dept': u'HMS', u'id': 5}