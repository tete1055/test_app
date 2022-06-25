from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext_lazy as _
from datetime import date
import uuid

# Create your models here.

# class UserManager(UserManager):
#     def _create_user(self, email, password, **extra_fields):
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_user(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(email, password, **extra_fields)

#     def create_superuser(self, email, password, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self._create_user(email, password, **extra_fields)

# class CustomUser(AbstractUser):
#     username = models.CharField(_('username'), max_length=150, blank=True)
#     email = models.EmailField(_('email address'), unique=True)

#     objects = UserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

def image_directory_path(instance, filename):
    return 'photos/{}.{}'.format(str(uuid.uuid4()), filename.split('.')[-1])

class CustomUser(AbstractUser):
    email = models.EmailField('email', unique=True)
    image = models.ImageField('image', upload_to=image_directory_path)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']