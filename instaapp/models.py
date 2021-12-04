from django.db import models
import datetime as dt
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db.models.fields import related
from tinymce.models import HTMLField

class Images(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='image',null=True)
    name = models.CharField(max_length=50)
    image = CloudinaryField('image')
    caption = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    like_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)

    def save_image(self):
        self.save()


    def update_caption(self, new_caption):
        self.image_caption = new_caption
        self.save()

    @classmethod
    def get_images_by_user(cls, user):
        images = cls.objects.filter(user=user)
        return images


    def delete_image(self):
        self.delete()

    @classmethod
    def search_by_image_name(cls, search_term):
        images = cls.objects.filter(
            image_name__icontains=search_term)
        return images

    
    @classmethod
    def get_single_image(cls, id):
        image = cls.objects.get(id=id)
        return image

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = CloudinaryField('image')
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    contact = models.CharField(max_length=50, blank=True, null=True)

    def update(self):
        self.save()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_profile_by_user(cls, user):
        profile = cls.objects.filter(user=user)
        return profile

    def __str__(self):
        return self.user.username

class Likes(models.Model):
    image = models.ForeignKey(Images, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.likes



class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Images, on_delete=models.CASCADE)
    comment = models.CharField(max_length=50)
    comment_date = models.DateTimeField(auto_now_add=True)

    def save_comment(self):
        self.save()

    def __str__(self):
        return self.comment

class Profiles(models.Model):
    profile_photo = CloudinaryField('image')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    posts = HTMLField()
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)
    message = models.IntegerField(default=0)
    follow = models.IntegerField(default=0)
    