from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from random import randint
from rest_framework.response import Response
from .utils import sms_send
from rest_framework import status
from .serializers import UserRegisterSerializer
# Create your views here.


class UserRegisterView(CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserRegisterSerializer
'''
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        number = request.data['phone_number']
        otp = randint(10000, 99999)

        user = get_user_model().objects.update_or_create(phone_number=number, defaults={'otp':otp})
        #if phone_number=number is exists: update otp; else create obj with data phone_number=number,defaults all

        #sms_send(number, otp)

        request.session['phone_number'] = number
        msg = {'messages':'please check sms and get otp'}

        return Response(msg, status=status.HTTP_302_FOUND)
'''
