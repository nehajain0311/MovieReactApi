from django.db import models

# Create your models here.
class Movie(models.Model):
    def __str__(self):
        return self.name
    name=models.CharField(max_length=100,unique=True)
    description=models.CharField(max_length=200)
    ratings=models.FloatField()
    #added later, default is provided to fetch image for non-user provided images
    image=models.ImageField(upload_to='images', default='images/default.jpg') #upload_to is the folders where images from user will be stored
    
