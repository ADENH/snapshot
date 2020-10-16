from django.db import models
from django_resized import ResizedImageField

# Create your models here.
def uploaded_location(instance, filename):
    return ("%s/%s") %(instance.nickname,filename)

class Team(models.Model):
    name = models.CharField(max_length=250)
    nickname = models.CharField(max_length=15)
    position = models.CharField(max_length=50)
    shortWord = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    # image = models.ImageField(upload_to=uploaded_location,null=True, blank=True, width_field="width_field", height_field="height_field")
    image = ResizedImageField(size=[220, 220], crop=['middle', 'center'], quality=90, upload_to=uploaded_location,null=True, blank=True, width_field="width_field", height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    def __str__(self):
        return self.nickname
    
    def get_absolute_url(self):
        return "/team/%s/" % (self.id)
