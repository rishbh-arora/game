from django.db import models
from django.contrib.auth.models import User


class gameLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.BinaryField()
    duration = models.TimeField()
    finish = models.BooleanField()

    def __str__(self):
        return self.user.first_name
