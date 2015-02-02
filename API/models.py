from django.db import models


class Post(models.Model):
    # idUser
    # idLocation
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    text = models.TextField()
    enabled = models.BooleanField(default=True)

    class Meta:
        ordering = ('createdAt',)