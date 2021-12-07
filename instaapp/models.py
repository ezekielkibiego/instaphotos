from django.db import models
import datetime as dt
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Image(models.Model):
    image = CloudinaryField('image')
    photo_name = models.CharField(max_length=60)
    posted_at = models.DateTimeField(auto_now_add=True)
    photo_caption = models.TextField()
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    liked= models.ManyToManyField(User,default=None,blank=True,related_name='liked')

    def save_image(self):
        self.save()


    @classmethod
    def display_photos(cls):
      photos = cls.objects.all().order_by('-posted_at')
      return photos
    
    
    @property
    def saved_likes(self):
      return self.photolikes.count()
    
    @classmethod
    def search_by_photo_name(cls,search_term):
        instaapp = cls.objects.filter(photo_name__icontains=search_term)
        return instaapp
    
    def delete_post(self):
      self.delete()

    @property
    def saved_comments(self):
        return self.comments.all()
    
    def __str__(self):
     return "%s photo" % self.photo_name


class Profile(models.Model):
    profile_photo = CloudinaryField('image')
    bio = models.TextField(null=True)
    user = models.OneToOneField(User,on_delete = models.CASCADE)


    @receiver(post_save , sender = User)
    def create_profile(instance,sender,created,**kwargs):
      if created:
        Profile.objects.create(user = instance)

    @receiver(post_save,sender = User)
    def save_profile(sender,instance,**kwargs):
      instance.profile.save()

    @property
    def saved_followers(self):
      return self.followers.count()   

    @property
    def saved_following(self):
      return self.following.count() 


    @property
    def follows(self):
      return [follow.followee for follow in self.following.all()]

    @property
    def following(self):
      return self.followers.all()



    

class Follow(models.Model):
  follower = models.ForeignKey(Profile, related_name='following',on_delete = models.CASCADE)
  followee = models.ForeignKey(Profile, related_name='followers',on_delete = models.CASCADE)

  def __str__(self):
    return "%s follower" % self.follower

LIKE_CHOICES={
    ('Like','Like'),
    ('Unlike','Unlike',)
}
class Like(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    value = models.CharField(choices=LIKE_CHOICES,default='like',max_length=10)

    def _str_(self):
        return self.value

class Comment(models.Model):
    comment = models.CharField(max_length=250,null=True)
    image = models.ForeignKey(Image,on_delete = models.CASCADE,related_name='comments',null=True)
    user = models.ForeignKey(User,on_delete = models.CASCADE,related_name='comments',null=True)

    @classmethod
    def display_comment(cls,image_id):
        comments = cls.objects.filter(image_id = image_id)
        return comments

