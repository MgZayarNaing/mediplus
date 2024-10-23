from django.db import models

# Create your models here.

class ImagesliderModel(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='imageslider')
    desc =  models.TextField()

    def str (self):
        return self.title