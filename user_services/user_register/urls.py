from django.urls import path
from .views import UserRegisterView, UserLoginView, UserDetailView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name = 'registration'),
    path('login/', UserLoginView.as_view(), name = 'login'),
    path('information/', UserDetailView.as_view(), name = 'information'),
]