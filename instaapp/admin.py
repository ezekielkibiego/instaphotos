from django.contrib import admin
from .models import Comments, Images, Likes,Profile,Profiles

admin.site.register(Images)
admin.site.register(Profile)
admin.site.register(Likes)
admin.site.register(Comments)
admin.site.register(Profiles)
