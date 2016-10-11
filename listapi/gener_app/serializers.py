from rest_framework import serializers
from .models import gener_api
class apiSerializer(serializers.ModelSerializer):
    class Meta:
        model = gener_api
        