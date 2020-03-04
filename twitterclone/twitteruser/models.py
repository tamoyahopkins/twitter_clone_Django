from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.utils import timezone

class MyCustomUser(AbstractUser):
    # can also add addtl fields like favorite color EG:
        # favorite_color = models.CharField(max_length=20)
        # home_page = models.URLField(null=True, blank=True)
    user_name = models.CharField(max_length=20)
    following = models.ManyToManyField('self', symmetrical=False)

    # following = models.ManyToManyField(user_name)

    def __str__(self):
        return self.username

# class Ticket(models.Model):
#     title = models.CharField(max_length=300)
#     posted_date = models.DateTimeField(default=timezone.now)
#     description = models.TextField()
#     status = models.CharField(max_length=50, default='New',
#         choices=[
#             ('Completed', 'Completed'),
#             ('In Progress', 'In Progress'),
#             ('Invalid', 'Invalid'),
#             ('New', 'New')
#         ])
#     filed_by = models.ForeignKey(
#         MyCustomUser,
#         on_delete=models.CASCADE,
#         related_name='filed_by',
#         null=True,
#         blank=True
#     )
#     assign_to_user = models.ForeignKey(
#         MyCustomUser,
#         null=True,
#         blank=True,
#         on_delete=models.CASCADE,
#         related_name='assign_to_user',
#     )
#     completed_by = models.ForeignKey(
#         MyCustomUser,
#         null=True,
#         blank=True,
#         on_delete=models.CASCADE,
#         related_name='completed_by'
#     )


