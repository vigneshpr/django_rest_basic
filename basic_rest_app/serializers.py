from rest_framework import serializers
from .models import Book
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        
        '''fields = ('firstname', 'lastname', 'dept', 'gender', 'language')
bookname = models.CharField(max_length=20, blank=True, unique=True)
    author = models.CharField(max_length=10, blank=True, default='')
    publication = models.CharField(max_length=30, blank=True, default='')
    dept = models.BooleanField(default=False)
    published_year'''