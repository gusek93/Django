from django.contrib import admin
from .models import Tweets


# admin 커스텀하기
@admin.register(Tweets)
class TweetAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'username', 'text', 'url']
