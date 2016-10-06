from rest_framework import serializers
from basic_rest_app.models import Student
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('firstname', 'lastname', 'dept', 'gender', 'language')
