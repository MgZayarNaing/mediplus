from django.db import models

# Create your models here.

class ImagesliderModel(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='imageslider')
    desc =  models.TextField()

    def __str__ (self):
        return self.title

class EmergencyCasesModel(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()

    def __str__(self):
        return self.title

class OpeningHoursModel(models.Model):
    day = models.CharField(max_length=100)
    time =  models.CharField(max_length=100)

    def  __str__(self):
        return self.day

