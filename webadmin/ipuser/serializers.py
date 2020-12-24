from rest_framework import serializers
from .models import IPUser


class IPUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPUser
        fields = '__all__'
