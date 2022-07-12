from django.contrib.auth import get_user_model
from rest_framework.authentication import BaseAuthentication, get_authorization_header
from rest_framework import exceptions
import jwt
from django.conf import settings

class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = get_authorization_header(request)
        if auth_header:
            auth_data = auth_header.decode('utf-8')

            auth_token = auth_data.split(" ")

            if len(auth_token) != 2:
                raise exceptions.AuthenticationFailed('token not valid')

            token = auth_token[1]

            try:
                payload = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')

                number = payload['phone_number']

                user = get_user_model().objects.get(phone_number=number)

                return (user, token)

            except jwt.ExpiredSignatureError as ex:
                raise exceptions.AuthenticationFailed('expire time token, please login agin')

            except jwt.DecodeError as ex:
                raise exceptions.AuthenticationFailed('token is invalid')

            except get_user_model().DoesNotExist as no_user:
                raise exceptions.AuthenticationFailed('user is not existsted')

