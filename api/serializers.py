from rest_framework.serializers import ModelSerializer
from .models import Bar, Special
from rest_framework import serializers


class SpecialSerializer(ModelSerializer):
    class Meta:
        model = Special
        fields = [
            'id', 
            'name',
            'days', 
            'details', 
            'bar'
        ]
class BarSerializer(ModelSerializer):
    # special = serializers.StringRelatedField(many=True)
    specials = SpecialSerializer(many=True)
    class Meta:
        model = Bar
        fields = [
            'id',
            'name',
            'address', 
            'hours',
            'specials'
        ]