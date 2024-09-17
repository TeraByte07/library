from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractUser
# Create your models here.

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)

class customUser(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique = True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    
from django.contrib.auth import get_user_model
from django.db import models

# Proxy model for admin users
class AdminUser(get_user_model()):
    class Meta:
        proxy = True
        verbose_name = 'Admin User'
        verbose_name_plural = 'Admin Users'
