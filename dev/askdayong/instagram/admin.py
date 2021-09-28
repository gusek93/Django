from django.contrib import admin
from .models import Post


#admin.site.register(Post)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # admin 에 표시 되는 내용들
    list_display = ['id', 'message', 'created_at', 'updated_at']
    list_display_links = ['message']
