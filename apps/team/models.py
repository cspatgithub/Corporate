from django.db import models
from ckeditor.fields import RichTextField


class Staff(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to='staff_images')
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.name