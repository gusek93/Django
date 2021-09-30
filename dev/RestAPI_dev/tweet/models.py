from django.db import models


# 모델 정의 tweet 정보
class Tweets(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    url = models.TextField(blank=True)
