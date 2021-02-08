from django.db import models

# Create your models here.

class Contact(models.Model):
    full_name= models.CharField(max_length=50)
    job_title = models.CharField(max_length=50 )
    email = models.EmailField(max_length=50)
    message = models.TextField(null = False)
    received_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name