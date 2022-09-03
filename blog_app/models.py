from django.db import models
from django.contrib.auth.models import User



STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Post (models.Model):                                #another instance cannot have the same name 
    title = models.CharField(max_length=200, unique=True) #unique means the title name has to be different 
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name ='blog_posts')
    updated_on =models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return self.title


class PostDump(models.Model):
    content = models.TextField()
    date_created =  models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.content
        

