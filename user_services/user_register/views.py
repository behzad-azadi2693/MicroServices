from django.shortcuts import render, HttpResponse
from rest_framework.generics import CreateAPIView, GenericAPIView, DestroyAPIView
from django.contrib.auth import get_user_model
from random import randint
from rest_framework.response import Response
from .utils import sms_send
from rest_framework import status
from .permissions import CheckSessionForNumbser
from .serializers import ( 
                UserRegisterSerializer, UserOtpLoginSerializer, UserTokenSerializer, 
                UserDetailSerializer, UserPasswordLoginSerializer
            )
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
import jwt
import datetime
from django.shortcuts import get_object_or_404

# Create your views here.


class UserRegisterView(CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserRegisterSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        number = str(request.data['phone_number'])
        otp = randint(10000, 99999)

        user = get_user_model().objects.update_or_create(
                                    phone_number=number, 
                                    defaults={'otp':jwt.encode({'otp':otp},settings.SECRET_KEY,algorithm='HS256')}
                                )
        #if phone_number=number is exists: update otp; else create obj with data phone_number=number,defaults all
        
        #sms_send(number, otp)
        print(otp, user[1])

        if user[1]:
            password = request.data['password']
            user[0].set_password(password)
            user[0].save()

        request.session['phone_number'] = number
        msg = {'messages':'please check sms and get otp'}

        return Response(msg, status=status.HTTP_302_FOUND)



class UserOtpLoginView(GenericAPIView):    
    serializer_class = UserOtpLoginSerializer
    permission_classes = [CheckSessionForNumbser]

    def post(self, request):
        otp = request.data['otp']
        number = str(request.session['phone_number'])
        get_user = get_object_or_404(get_user_model(), phone_number=number)

        payload = jwt.decode(get_user.otp, settings.SECRET_KEY, algorithms='HS256')

        if str(payload['otp']) != str(otp) and payload['exp'] < datetime.now():
            return Response({"message":"please check your sms and otp"}, status=status.HTTP_401_UNAUTHORIZED)

        if not get_user.is_active:
            get_user.is_active = True
            get_user.save()

        self.serializer_class = UserTokenSerializer
        serializer = self.serializer_class(get_user)

        return Response(serializer.data, status=status.HTTP_200_OK)
            

class UserPasswordLoginView(GenericAPIView):
    serializer_class = UserPasswordLoginSerializer

    def post(self, request):
        number = request.data['phone_number']
        password = request.data['password']

        get_user = get_object_or_404(get_user_model(), phone_number=number)

        user = authenticate(phone_number=number, password=password)

        if user:
            self.serializer_class = UserTokenSerializer
            serializer = self.serializer_class(user)

            return Response(serializer.data, status=status.HTTP_200_OK)
            
        return Response({"message":"please check your smms and otp"}, status=status.HTTP_401_UNAUTHORIZED)

class UserDetailView(DestroyAPIView):
    model = get_user_model()
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = get_user_model().objects.get(id=self.request.user.id)

        return user