from django.urls import path
from .views import UserRegister


app_name = 'user_register'


urlpatterns = [
    path('', UserRegister.as_view(), name='user_register'),
]
