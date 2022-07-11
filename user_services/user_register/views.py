from django.shortcuts import render, HttpResponse
from rest_framework.generics import CreateAPIView, GenericAPIView
from django.contrib.auth import get_user_model
from random import randint
from rest_framework.response import Response
from .utils import sms_send
from rest_framework import status
from .permissions import CheckSessionForNumbser
from .serializers import UserRegisterSerializer, UserLoginSerializer, UserTokenSerializer
from django.contrib.auth import authenticate

# Create your views here.


class UserRegisterView(CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserRegisterSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        number = request.data['phone_number']
        otp = randint(10000, 99999)

        user = get_user_model().objects.update_or_create(phone_number=number, defaults={'otp':otp})
        #if phone_number=number is exists: update otp; else create obj with data phone_number=number,defaults all
        
        #sms_send(number, otp)
        print(otp)
        user[0].set_password(str(otp))
        user[0].save()

        request.session['phone_number'] = number
        request.session['active'] = user[0].is_active
        msg = {'messages':'please check sms and get otp'}

        return Response(msg, status=status.HTTP_302_FOUND)


class UserLoginView(GenericAPIView):    
    serializer_class = UserLoginSerializer
    permission_classes = [CheckSessionForNumbser]

    def post(self, request):
        otp = request.data['otp']
        number = str(request.session['phone_number'])

        if request.session['active'] is False:
            get_user_model().objects.filter(phone_number=number).update(is_active=True)

        user = authenticate(phone_number=number, password=otp)

        if user:
            self.serializer_class = UserTokenSerializer
            serializer = self.serializer_class(user)

            return Response(serializer.data, status=status.HTTP_200_OK)
            
        return Response({"message":"please check your smms and otp"}, status=status.HTTP_401_UNAUTHORIZED)
        
