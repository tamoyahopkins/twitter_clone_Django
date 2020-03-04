from django.db import models
from django.utils import timezone
from twitteruser.models import MyCustomUser

# Create your models here.
class Tweet(models.Model):
    user = models.ForeignKey(
        MyCustomUser,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    text = models.CharField(max_length=140)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text

