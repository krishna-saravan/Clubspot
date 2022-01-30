from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

# Create your models here.

class UserAccountManager(BaseUserManager):
    def create_user(self,email,password = None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)

        user.set_password(password)
        user.save()

        return user

class UserAccount(AbstractBaseUser,PermissionsMixin):
    registration_number = models.CharField(max_length=10, null= False)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length= 255)
    last_name = models.CharField(max_length= 255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'