from django.contrib.auth.models import AbstractUser, User
from django.db import models
from core.base import TimeStampedModel


class MyUser(AbstractUser):
    pass


class Post(TimeStampedModel):
    user = models.ForeignKey('MyUser', on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=70)
    content = models.TextField()
    likes = models.ManyToManyField('MyUser', related_name='liked_posts', blank=True)

    @property
    def liked_posts(self):
        return self.likes.count()
    def __str__(self):
        return self.title


class ProfileUser(TimeStampedModel):
    user = models.OneToOneField('MyUser', on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return self.user.username
