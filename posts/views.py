from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Post
from .Serilizer import PostSerializer


@api_view(["GET", "POST"])
def posts(request):

    if request.method == "GET":

        serializer = PostSerializer(
            Post.objects.all(),
            many=True
        )

        return Response(serializer.data)

    serializer = PostSerializer(
        data=request.data
    )

    if serializer.is_valid():

        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )

    print(serializer.errors)

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

        serializer = PostSerializer(post)

        return Response(serializer.data)

    if request.method == "PUT":

        serializer = PostSerializer(
            post,
            data=request.data,
            partial=True,
        )

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        print(serializer.errors)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    post.delete()

    return Response(
        status=status.HTTP_204_NO_CONTENT
    )