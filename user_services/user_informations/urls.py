from django.urls import path
from .views import UserInformations


app_name = 'user_login'


urlpatterns = [
    path('', UserInformations.as_view(), name='user_informations'),
]