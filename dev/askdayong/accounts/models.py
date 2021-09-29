from django.conf import settings
from django.conf import settings
from django.db import models


# 1:n 관계 정의 
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=6)


