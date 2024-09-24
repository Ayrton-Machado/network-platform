
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("post", views.submit_post, name="post"),
    path("profile/<str:username>", views.load_profile, name="profile"),
    path("profile/<str:username>/follow", views.follow, name="follow"),
    path("following", views.load_following, name="following")
]
