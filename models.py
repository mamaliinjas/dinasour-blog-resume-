from django.db import models

# Create your models here.

class CarnivorousPost(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField()
    image_url=models.URLField(max_length=1000 ,blank=True , null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class herbivoresPost(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField()
    image_url=models.URLField(max_length=1000 ,blank=True , null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class pterosaursPost(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField()
    image_url=models.URLField(max_length=1000 ,blank=True , null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
