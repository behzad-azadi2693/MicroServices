from rest_framework import serializers
from django.contrib.auth import get_user_model
from random import randint
from rest_framework.response import Response

class UserRegisterSerializer(serializers.Serializer):
    phone_number = serializers.IntegerField()
    
    def validate_phone_number(self, value):
        if len(str(value)) != 10:
            raise serializers.ValidationError('phone number must of lenght 11')

        return value        

   
        
