from django.db import models


class BlogCategory(models.Model):
    category_name = models.CharField(null = False, max_length = 30)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.category_name
    
    class Meta:
        verbose_name = 'Blog Category'
        verbose_name_plural = 'Blog Categories'

class Blog(models.Model):
    title =models.CharField(null=False,max_length=100)
    image_file = models.ImageField(upload_to='pictures/', null = True)
    author = models.CharField(null = False, max_length = 50)
    description = models.TextField(null = False, max_length = 200)
    is_popular = models.BooleanField(null=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.category
    
    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'