from django.db import models
from django.contrib.auth.models import User


class Argument(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_argument')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question')  # 추천인 추가

    def __str__(self):
        return self.subject


class Refute(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_refute')
    argument = models.ForeignKey(Argument, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_refute')
