from django.conf import settings
from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(null=False, max_length=255)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    hit_count = models.BigIntegerField(default=0, null=True, blank=True)
    last_hit = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class Quote(models.Model):
    author = models.ForeignKey('quote.Author')
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    context = models.CharField(max_length=255, null=True, blank=True)
    hit_count = models.BigIntegerField(default=0, null=True, blank=True)
    last_hit = models.DateTimeField(null=True, blank=True)
    image = models.FileField(upload_to=settings.STATIC_ROOT + '/uploads/', null=True, blank=True)

    def __str__(self):

        if self.author.name == 'debug':
            return self.text

        return '{} - {}'.format(self.text, self.author.name)