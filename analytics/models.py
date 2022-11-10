from ipaddress import ip_address
from django.db import models

# Create your models here.
class UserTrack(models.Model):
    ip_address = models.GenericIPAddressField()
    user_agent = models.CharField(max_length=200)
    url        = models.CharField(max_length=100)
    visited_at = models.DateTimeField(auto_now_add=True)

