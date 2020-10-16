from django.db import models
from django_resized import ResizedImageField

# Create your models here.
def uploaded_location(instance, filename):
    return ("%s/%s") %(instance.name,filename)

class Company(models.Model):
    name = models.CharField(max_length=250)
    tagline = models.CharField(max_length=250)
    logo = ResizedImageField(size=[520, 520], crop=['middle', 'center'], quality=100, upload_to=uploaded_location,null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    facebook = models.CharField(max_length=250,null=True, blank=True)
    instagram = models.CharField(max_length=250,null=True, blank=True)
    twitter = models.CharField(max_length=250,null=True, blank=True)
    linkedin = models.CharField(max_length=250,null=True, blank=True)
    googleplus =models.CharField(max_length=250,null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return "/company/%s/" % (self.id)