from django.contrib.auth.models import User
from django.db import models


class Cards(models.Model):
    cardname = models.CharField(max_length=64)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cardnos = models.IntegerField()

    class Meta:
        ordering = ['cardname']
        verbose_name = 'Card'
        verbose_name_plural = 'Card'
