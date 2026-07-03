from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Post
from .Serilizer import PostSerializer


@api_view(["GET", "POST"])
def posts(request):

    if request.method == "GET":

        posts = Post.objects.all().order_by("-created_at")

        serializer = PostSerializer(
            posts,
            many=True,
            context={"request": request},
        )

        return Response(serializer.data)

    serializer = PostSerializer(
        data=request.data,
        context={"request": request},
    )

    if serializer.is_valid():

        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST,
    )


@api_view(["GET", "PUT", "DELETE"])
def post_detail(request, pk):

    try:
        post = Post.objects.get(pk=pk)

    except Post.DoesNotExist:

        return Response(
            {"error": "Post not found"},
            status=status.HTTP_404_NOT_FOUND,
        )

    if request.method == "GET":

        serializer = PostSerializer(
            post,
            context={"request": request},
        )

        return Response(serializer.data)

    if request.method == "PUT":

        old_image = post.image

        serializer = PostSerializer(
            post,
            data=request.data,
            partial=True,
            context={"request": request},
        )

        if serializer.is_valid():

            serializer.save()

            # Delete previous image if replaced
            if (
                old_image
                and request.FILES.get("image")
                and old_image.path != post.image.path
            ):
                import os

                if os.path.isfile(old_image.path):
                    os.remove(old_image.path)

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    post.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)