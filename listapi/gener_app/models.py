from __future__ import unicode_literals
from django.db import models

class gener_api(models.Model):
    bookname = models.CharField(max_length=20, blank=True, unique=True)
    author = models.CharField(max_length=10, blank=True, default='')
    publication = models.TextField(max_length=30)
    dept = models.CharField(max_length=30)
    published_year= models.IntegerField(default=0)
    
    class Meta:
        ordering = ('bookname',)
