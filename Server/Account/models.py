from django.db import models
from django.contrib.auth.models import UserManager, AbstractUser

# Create your models here.

class Team(models.Model):
    name = models.CharField(verbose_name='Team name', max_length=255)
    # pilot nhu

    def __str__(self):
        return f"{self.id}, {self.name}"

class User(AbstractUser):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True, default=1)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.username

