from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import jwt
from django.conf import settings
from datetime import datetime, timedelta
# Create your models here.


class  MyUserManager(BaseUserManager):
    def create_user(self, phone_number, password):
        if not phone_number:
            raise ValueError("please insert phone number")
        user = self.model(phone_number=phone_number)
        user.set_password(password)
        user.save(using=self._db)
        return user 

    def create_superuser(self, phone_number, password):
        user = self.create_user(phone_number=phone_number, password=password)
        user.is_admin=True
        user.save(using=self._db)
        return user
 

class User(AbstractBaseUser,PermissionsMixin):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{11,11}$', message="Phone number must be entered in the format: '+999999999'. Up to 11 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=11,unique=True, verbose_name="your phone number") # validators should be a list
    otp = models.PositiveIntegerField(null=True, blank=True)
    otp_create_time = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    is_active = models.BooleanField(default=False, verbose_name="user is active")
    is_admin = models.BooleanField(default=False, verbose_name="user is admin")
    
    objects=MyUserManager()
    USERNAME_FIELD = 'phone_number'
    
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self) -> str:
        return self.phone_number

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
        
    @property
    def is_staff(self):
        return self.is_admin

    @property
    def token(self):
        token = jwt.encode({'phone_number': self.phone_number, 'id': self.id, 'active':self.is_active, 'exp': datetime.now() + timedelta(days=15)}, 
                           settings.SECRET_KEY, 
                           algorithm='HS256'
                        )
        return token