from django.db import models


class AboutMe(models.Model):
    name = models.CharField(null = False, max_length = 30)
    image_file = models.ImageField(upload_to='pictures/', null = True)
    job_title = models.CharField(max_length = 100)
    description = models.TextField(null = False, max_length = 200)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'About Me'
        verbose_name_plural = 'About Me'

class Timeline(models.Model):
    date = models.DateField()
    title = models.CharField(null = False, max_length = 100)
    details =  models.CharField(null = False, max_length = 200)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Timeline'
        verbose_name_plural = 'Timelines'

class Expertise (models.Model):
    name = models.CharField(null=False ,max_length=50)
    image_file =  models.ImageField(upload_to='uploads/', null= True)
    created_at = models.DateField(null = False, auto_now=True)
    updated_at = models.DateField(null = False, auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('-created_at',)
