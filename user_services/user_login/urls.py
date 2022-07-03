from django.urls import path
from .views import UserLogout, UserLogin


app_name = 'user_login'


urlpatterns = [
    path('login/', UserLogin.as_view(), name='user_login'),
    path('logout/', UserLogout.as_view(), name='user_logout'),
]
