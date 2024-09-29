from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import User, Post

def index(request):
    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "network/index.html", {
        "posts": posts,
        "user": request.user,
        "page_obj": page_obj
    })

@csrf_exempt
def edit_post(request, post_id):
    if request.method == "POST":
        post = Post.objects.get(id=post_id)
        content_edited = request.POST[f"edit_post{post_id}"]

        post.content = content_edited
        post.save()
        return JsonResponse({'success': True, 'new_content': post.content})

def load_following(request):
    user = request.user

    return render(request, "network/following.html", {
        "user_following": user.following.all()
    })

def load_profile(request, username):
    user = User.objects.get(username=username)
    
    return render(request, 'network/profile.html', {
        "profile": user,
        "posts": user.posts.all().order_by('-created_at'),
        "followers": user.followers.all()
    })

def follow(request, username):
    user = User.objects.get(username=username)
    current_user = request.user

    if current_user in user.followers.all():
        current_user.following.remove(user)
        return HttpResponseRedirect(reverse('profile', kwargs={'username': username}))
    
    current_user.following.add(user)
    return HttpResponseRedirect(reverse('profile', kwargs={'username': username}))

def submit_post(request):
    if request.method == "POST":

        user = request.user
        content = request.POST["post_content"]

        Post(user=user, content=content).save()
        return HttpResponseRedirect(reverse("index"))

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
