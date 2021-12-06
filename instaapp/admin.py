from django.contrib import admin
from .models import Comment, Follow, Image, Like,Profile

admin.site.register(Image)
admin.site.register(Profile)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Follow)
