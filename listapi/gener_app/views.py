#from django.shortcuts import render
from rest_framework import generics
from django.core import serializers
from gener_app.models import *
from gener_app.serializers import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
# from django.http import HttpResponse
# Create your views here.

class listget(generics.RetrieveUpdateAPIView):
	queryset = gener_api.objects.all()
	serializer_class = apiSerializer

# class listcreate(APIView): #post
@csrf_exempt
@api_view(('POST',))	
def demo(request):
	if request.method == 'POST':
		data = JSONParser().parse(request)
		# print data1
		# data={'published_year': 1978, 'publication': 'Mathi', 'author': 'Selvi', 'bookname': 'CC', 'dept': 'SE'}
		serializer = apiSerializer(data=data)
        if serializer.is_valid():
        	serializer.save()
        	#print serializer.data
        	return Response(serializer.data, status=status.HTTP_201_CREATED)
        	
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)	

class listdel(generics.DestroyAPIView): #delete
	queryset = gener_api.objects.all()
	serializer_class = apiSerializer

class listupdate(generics.UpdateAPIView): #update
	queryset = gener_api.objects.all()
	serializer_class = apiSerializer

	#{'published_year': 1984, 'publication': u'radha', 'author': u'annie', 'bookname': u'EVS', 'dept': u'HMS', u'id': 5}