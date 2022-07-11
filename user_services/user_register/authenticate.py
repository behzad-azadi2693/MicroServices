from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class PhoneLoginBackend(ModelBackend):
    def authenticate(self, request, phone_number=None, password=None):
        try:
            user = get_user_model().objects.get(phone_number = phone_number)
            if user.check_password(password):
                return user
            return None

        except user.DosNotExist:
            return None
    
    def get_user(self, user_id):
        try:
            return User.objects.get(id=user_id)
        
        except User.DosNotExist:
            return None