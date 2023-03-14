from django.db import models
from app.functions import create_shortened_url

# Create your models here.


class Shortener(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    times_followed = models.PositiveIntegerField(default=0)
    their_url = models.URLField()
    my_url = models.CharField(max_length=15, unique=True, blank=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f'from {self.their_url} to {self.my_url}'

    def save(self, *args, **kwargs):
        if not self.my_url:
            self.my_url = create_shortened_url(self)
        super().save(*args, **kwargs)
