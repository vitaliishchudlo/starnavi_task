from django.db import models
from django.utils import timezone
from users.models import User


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user} | {self.created}'


class Publication(models.Model):
    title = models.CharField(max_length=150)
    body = models.CharField(max_length=150, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publications')
    likes = models.ManyToManyField(Like, related_name='publications', null=True, blank=True)

    def __str__(self):
        return self.title
