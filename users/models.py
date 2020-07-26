from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class User(AbstractUser):
    nickname = models.CharField(max_length=15, null=False, unique=True)
    username = models.CharField(max_length=10, null=False, unique=False)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    def __str__(self):
        return self.nickname

    USERNAME_FIELD = 'nickname'
    REQUIRED_FIELDS = ['username',]
    