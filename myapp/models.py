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

class ExpModel(models.Model):
    total_exp = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)

    def __str__(self):
        return self.total_exp

class FeatureModel(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    img = models.ImageField(upload_to='feature/', null=True,blank=True)

    def  __str__(self):
        return self.title

class WhoWeAreModel(models.Model):
    title = models.CharField(max_length=200)
    desc1 = models.TextField()
    desc2 = models.TextField()

    def  __str__(self):
        return self.title

class WhoWeAreListModel(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text
    

class WhoWeAreVideoModel(models.Model):
    name = models.CharField(max_length=200)
    video  = models.FileField(upload_to='WhoWeAreVideoModel/')

    def __str__(self):
        return self.name
    

class ContactModel(models.Model):
    title  = models.CharField(max_length=200)
    desc = models.TextField()
    phone  = models.CharField(max_length=100)

    def  __str__(self):
        return self.title






