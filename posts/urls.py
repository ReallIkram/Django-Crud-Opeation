from django.urls import path
from . import views

urlpatterns = [

    path("posts/", views.posts),

    path(
        "posts/<int:pk>/",
        views.post_detail,
    ),

]