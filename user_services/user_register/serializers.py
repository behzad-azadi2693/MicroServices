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

   
class UserLoginSerializer(serializers.Serializer):
    otp = serializers.IntegerField()
    
    def validate_phone_number(self, value):
        if len(str(value)) != 5 and isinstance(value, int):
            raise serializers.ValidationError('please check your sms for otp')

        return value       


class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('phone_number','id','token')

        read_only_fields = ['phone_number','id','token']