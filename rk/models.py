from django.db import models
    # Create your models here.

class Deed(models.Model):
     title = models.CharField(max_length=120)
     detail = models.TextField()
     done = models.BooleanField(default=False)

     def __str__(self):
         return self.title
