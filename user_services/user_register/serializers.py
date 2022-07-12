from rest_framework import serializers
from django.contrib.auth import get_user_model
from random import randint
from rest_framework.response import Response
import re

class UserRegisterSerializer(serializers.Serializer):
    phone_number = serializers.IntegerField(required=True)
    password = serializers.CharField(required=True)
    password_confirm = serializers.CharField(required=True)

    def validate_phone_number(self, value):
        print(str(value))
        if not re.findall(r'^9\d{9}$', str(value)):
            raise serializers.ValidationError('please check your phone number')

        return value        

    def validate_password_confirm(self, value):
        data = self.get_initial()
        password = data.get('password')
        password_confirm = value

        if not re.findall(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$", password):
            raise serializers.ValidationError('Minimum eight characters, at least one letter, one number and one special character')

        if password_confirm != password:
            raise serializers.ValidationError('password and password confirm not matching')

        return value


class UserOtpLoginSerializer(serializers.Serializer):
    otp = serializers.IntegerField()
    
    def validate_otp(self, value):
        if len(str(value)) != 5 and isinstance(value, int):
            raise serializers.ValidationError('please check your sms for otp')

        return value       


class UserPasswordLoginSerializer(serializers.Serializer):
    phone_number = serializers.IntegerField(required=True)
    password = serializers.CharField(required=True)

    def validate_phone_number(self, value):
        print(str(value))
        if not re.findall(r'^9\d{9}$', str(value)):
            raise serializers.ValidationError('please check your phone number')

        return value        

    def validate_password(self, value):
        data = self.get_initial()
        password = value

        if not re.findall(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$", password):
            raise serializers.ValidationError('Minimum eight characters, at least one letter, one number and one special character')


class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('phone_number','id','token')

        read_only_fields = ['phone_number','id','token']


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'phone_number', 'is_active', 'is_admin')