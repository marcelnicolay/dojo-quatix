from django.contrib import admin
from blog.core.models import Post, Tag

admin.site.register(Post)
admin.site.register(Tag)