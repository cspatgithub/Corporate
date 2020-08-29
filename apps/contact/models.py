from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.template.defaultfilters import slugify


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=14)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    is_read = models.BooleanField(default=False)

    slug = models.SlugField(default='')
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return self.name + ' - ' + self.subject
    
    def get_absolute_url(self):
        return reverse('contact-detail', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.date)
        return super(Contact, self).save(*args, **kwargs)