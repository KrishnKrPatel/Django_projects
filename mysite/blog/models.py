from django.db import models

# Create your models here.
class Blogpost(models.Model):
    title=models.CharField(max_length=240)
    author=models.CharField(max_length=240,db_index=True)
    body=models.TextField()

    published=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)