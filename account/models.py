from django.contrib.auth.models import AbstractUser
from django.db import models 


class User(AbstractUser):
    image = models.ImageField(upload_to='media/profile')
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.username