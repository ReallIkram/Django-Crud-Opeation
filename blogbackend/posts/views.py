from django.shortcuts import render, redirect, get_object_or_404
from .models import Post


def home(request):

    posts = Post.objects.all().order_by("-created_at")

    context = {
        "posts": posts
    }

    return render(request, "posts/home.html", context)


def create_post(request):

    if request.method == "POST":

        Post.objects.create(
            title=request.POST.get("title"),
            content=request.POST.get("content")
        )

        return redirect("home")

    return render(request, "posts/create.html")


def update_post(request, id):

    post = get_object_or_404(Post, id=id)

    if request.method == "POST":

        post.title = request.POST.get("title")
        post.content = request.POST.get("content")

        post.save()

        return redirect("home")

    context = {
        "post": post
    }

    return render(request, "posts/create.html", context)


def delete_post(request, id):

    post = get_object_or_404(Post, id=id)

    if request.method == "POST":

        post.delete()

        return redirect("home")

    return render(request, "posts/delete.html", {"post": post})