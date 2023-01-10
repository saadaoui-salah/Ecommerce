from django.contrib.auth.models import AbstractUser
from django.db import models 


class User(AbstractUser):
    image        = models.ImageField(upload_to='media/profile')
    address      = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    user_type    = models.CharField(
        max_length=20, 
        choices=[
                ('SELLER', 'SELLER'), 
                ('BUYER', 'BUYER'), 
                ('ADMIN', 'ADMIN')
            ]
        )

    def __str__(self) -> str:
        return self.username
    
    def is_seller(self):
        return self.user_type == 'SELLER'
    
    def is_buyer(self):
        return self.user_type == 'BUYER'