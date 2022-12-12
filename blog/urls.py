from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name="sarting-page"),
    path("posts", views.posts, name="posts-page"),
    path("posts/<slug:slug>", views.posts, name="post-details-page"),
]