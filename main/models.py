
from django.db import models

from slugify import slugify

class Entry(models.Model):
    Name = models.CharField( max_length=15,blank=False,null=False)
    Email = models.EmailField(max_length=30)
    time = models.DateTimeField(auto_now_add=True)
    Quote= models.TextField(blank=True, null=False)

    class Meta:
        db_table = 'Blog_Entry'
        verbose_name_plural = "Blog"

    
