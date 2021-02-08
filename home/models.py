from django.db import models
from blog.models import Blog

class Banner(models.Model):
    title= models.CharField(max_length=50)
    sub_title = models.CharField(max_length=50 )
    image_file = models.ImageField(upload_to='pictures/', null = True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Subscription(models.Model):
    email = models.EmailField(max_length=50)
    received_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
    