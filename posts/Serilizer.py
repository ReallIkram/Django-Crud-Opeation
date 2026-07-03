from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = "__all__"

    def to_representation(self, instance):

        data = super().to_representation(instance)

        if instance.image:

            url = instance.image.url

            if url.startswith("http://"):
                url = url.replace("http://", "https://", 1)

            data["image"] = url

        else:
            data["image"] = None

        return data