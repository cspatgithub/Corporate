from django.db import models
from ckeditor.fields import RichTextField


class Service(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=30)
    details = RichTextField()

    def __str__(self):
        return self.name
    
    
