from django.db import models

class Student(models.Model):
    firstname = models.CharField(max_length=100, blank=True, default='')
    lastname = models.CharField(max_length=100, blank=True, default='')
    dept = models.TextField()
    gender = models.BooleanField(default=False)
    language = models.CharField(default='python', max_length=100)
    
    class Meta:
        ordering = ('firstname',)