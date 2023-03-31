from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    STATUS = ((0, "Draft"), (1, "Publish"))
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated_on', '-created_on'] 
    
    def __str__(self):
        return self.title

  
class Comment(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE)  
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    body = models.TextField()
    update_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.body[0:50]
