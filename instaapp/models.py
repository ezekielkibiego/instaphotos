from django.db import models
import datetime as dt
from cloudinary.models import CloudinaryField



class Images(models.Model):
    name = models.CharField(max_length=50)
    image = CloudinaryField('image')
    caption = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def save_image(self):
        self.save()


    # update image
    def update_caption(self, name, description):
        self.name = name
        self.description = description
    
        self.save()
        

    @classmethod
    def get_all_images(cls):
        images = Images.objects.all()
        return images

    def delete_image(self):
        self.delete()

    

    def __str__(self):
        return self.name