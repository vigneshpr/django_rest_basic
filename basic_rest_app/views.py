from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from basic_rest_app.models import Student
from basic_rest_app.serializers import StudentSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)
	
@csrf_exempt
def student_list(request):
    
    if request.method == 'GET':
        basic_rest = Student.objects.all()
        serializer_rest_get = StudentSerializer(basic_rest, many=True)
        return JSONResponse(serializer_rest_get.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer_rest_post = StudentSerializer(data=data)
        if serializer_rest_post.is_valid():
            serializer_rest_post.save()
            return JSONResponse(serializer_rest_post.data, status=201)
        return JSONResponse(serializer_rest_post.errors, status=400)      

@csrf_exempt
def student_detail(request, pk):
   
    try:
        student_detail = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer_get = StudentSerializer(student_detail)
        return JSONResponse(serializer_get.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer_put = StudentSerializer(student_detail, data=data)
        if serializer_put.is_valid():
            serializer_put.save()
            return JSONResponse(serializer_put.data)
        return JSONResponse(serializer_put.errors, status=400)

    elif request.method == 'DELETE':
        student_detail.delete()
        return HttpResponse(status=204)