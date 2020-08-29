from django.db import models
from ckeditor.fields import RichTextField


class Detail(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()

    def __str__(self):
        return self.title


class Review(models.Model):
    client_name = models.CharField(max_length=100)
    role = models.CharField(default='', max_length=100)
    image = models.FileField(upload_to='client_images')
    review_text = models.TextField()
