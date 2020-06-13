from django.contrib.auth.models import User
from django.db import models


class Cards(models.Model):
    class ColorChoice(models.TextChoices):
        BLUE = 'blue'
        RED = 'red'
        GREEN = 'green'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cards")
    title = models.CharField(max_length=30, null=True)
    contents = models.TextField(null=True)
    created_at = models.DateTimeField(null=True)
    is_reported = models.BooleanField(default=False)
    color = models.CharField(choices=ColorChoice.choices, max_length=30, null=True)
