from django.db import models
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.FileField(upload_to='post_images')
    text = RichTextField()
    date = models.DateTimeField(default=timezone.now)

    slug = models.SlugField(default='')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.slug})
    
    class Meta:
        ordering = ['-date']
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Post, self).save(*args, **kwargs)

