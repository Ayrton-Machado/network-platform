
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("post", views.submit_post, name="post"),
    path("profile/<str:username>", views.load_profile, name="profile"),
    path("following", views.load_following, name="following"),

    #API's
    path("edit/<int:post_id>", views.edit_post, name="edit_post"),
    path("like/<int:post_id>", views.like_post, name="like_post"),
    path("profile/<str:username>/follow", views.follow, name="follow")
]
