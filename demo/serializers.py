from rest_framework import serializers
from .models import Events

class Eventserializer(serializers.ModelSerializer):
    class Meta:
        model =Events
        fields='__all__'

