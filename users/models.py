from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    chat_id = models.CharField(max_length=10, verbose_name='чат', **NULLABLE, default="884314581")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
