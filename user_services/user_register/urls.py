from django.urls import path
from .views import UserRegisterView, UserOtpLoginView, UserDetailView, UserPasswordLoginView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name = 'registration'),
    path('otp/login/', UserOtpLoginView.as_view(), name = 'ot_login'),
    path('password/login/', UserPasswordLoginView.as_view(), name = 'password_login'),
    path('information/', UserDetailView.as_view(), name = 'information'),
]