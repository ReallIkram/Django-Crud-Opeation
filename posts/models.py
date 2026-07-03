from django.db import models
import os


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    image = models.ImageField(
        upload_to="posts/",
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    # Delete image file when post is deleted
    def delete(self, *args, **kwargs):

        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)

        super().delete(*args, **kwargs)