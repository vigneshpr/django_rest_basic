from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

@api_view(['GET', 'POST'])
def student_list(request, format=None):
    
    if request.method == 'GET':
        basic_rest = Student.objects.all()
        serializer_rest_get = StudentSerializer(basic_rest, many=True)
        return Response(serializer_rest_get.data)

    elif request.method == 'POST':
        serializer_rest_post = StudentSerializer(data=request.data)
        if serializer_rest_post.is_valid():
            serializer_rest_post.save()
            return Response(serializer_rest_post.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, pk, format=None):
   
    try:
        student_detail = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
         return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer_get = StudentSerializer(student_detail)
        return Response(serializer_get.data)

    elif request.method == 'PUT':
        serializer_put = StudentSerializer(student_detail, data=request.data)
        if serializer_put.is_valid():
            serializer_put.save()
            return Response(serializer_put.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)