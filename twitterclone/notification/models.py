from django.db import models
from twitteruser.models import MyCustomUser
from tweet.models import Tweet

# Create your models here.

class Notification(models.Model):
    for_user = models.ForeignKey(
        MyCustomUser,
        on_delete= models.CASCADE
    )
    source_tweet = models.ForeignKey(
        Tweet,
        on_delete=models.CASCADE
    )
    viewed = models.BooleanField(default=False)
    def __str__(self):
        return self.source_tweet.text