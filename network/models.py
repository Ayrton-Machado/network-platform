from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    following = models.ManyToManyField('self', related_name='followers', symmetrical=False)

    def __str__(self):
        return f'Username: {self.username}\nEmail: {self.email}\nLast Login: {self.last_login}'

class Post(models.Model):
    user = models.ForeignKey(User, related_name="posts",on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Username: {self.user}\nContent: {self.content}\n{self.created_at}'

