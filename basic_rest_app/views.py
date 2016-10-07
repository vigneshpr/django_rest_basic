from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

@api_view(['GET', 'POST'])
def student_list(request,pk=None, format=None):
    
    if request.method == 'GET':
        basic_rest = Book.objects.all()
        serializer_rest_get = BookSerializer(basic_rest  , many=True)
        return Response(serializer_rest_get.data)

    elif request.method == 'POST':
        serializer_rest_post = BookSerializer(data=request.data)
        if serializer_rest_post.is_valid():
            serializer_rest_post.save()
            return Response(serializer_rest_post.data, status=status.HTTP_201_CREATED)
        return Response(serializer_rest_post.errors, status=status.HTTP_400_BAD_REQUEST)

    

@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, pk, format=None):
   
    try:
        student_detail = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
         return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer_get = BookSerializer(student_detail)
        return Response(serializer_get.data)

    elif request.method == 'PUT':
        serializer_put = BookSerializer(student_detail, data=request.data)
        if serializer_put.is_valid():
            serializer_put.save()
            return Response(serializer_put.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)