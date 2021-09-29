from django.contrib import admin
from .models import Post, Comment, Tag
from django.utils.safestring import mark_safe


#admin.site.register(Post)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # admin 에 표시 되는 내용들
    list_display = ['id', 'photo_tag','message', 'message_length', 'is_public', 'created_at', 'updated_at']
    list_display_links = ['message']
    list_filter = ['message', 'is_public']
    search_fields = ['message']

    def photo_tag(self, post):
        if post.photo:
            return mark_safe(f'<img src= "{post.photo.url}" style="width: 50px"/>')
        return None

    def message_length(self, post):
        return f"{len(post.message)} 글자"

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass