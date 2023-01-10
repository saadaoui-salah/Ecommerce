from django.contrib.auth.models import AbstractUser
from django.db import models 


class User(AbstractUser):
    image = models.ImageField(upload_to='media/profile')

    def __str__(self) -> str:
        return self.username