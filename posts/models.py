from django.db import models
from cloudinary.models import CloudinaryField


class Post(models.Model):

    title = models.CharField(max_length=200)

    content = models.TextField()

    image = CloudinaryField(
        "image",
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title