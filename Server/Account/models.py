from typing import overload
from django.db import models
from django.contrib.auth.models import UserManager, AbstractUser

# Create your models here.
# class Manager(UserManager):

#     def create_user(self, username: str, email: Optional[str] = ..., password: Optional[str] = ..., **extra_fields: Any) -> _T:
#         team = Team.objects.filter(name = ' ')
#         return super().create_user(username, email, password, team_id, **extra_fields)
#     def create_user(self, username, email, team_id, password=None):
#         if not username:
#             raise ValueError("Username is required!")
#         if not email:
#             raise ValueError("Please provide an active email")

#         user = self.model(
#             username = username,
#             email = self.normalize_email(email),
#             team_id = team_id
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self,  username, email, team_id, password=None):
#         user = self.create_user(
#             username=username,
#             email=email,
#             team_id=team_id,
#             password=password
#         )
#         user.is_admin = True
#         user.is_superuser = True
#         user.is_staff = True
    
#         user.save(using=self._db)
#         return user


class Team(models.Model):
    name = models.CharField(verbose_name='Team name', max_length=255)

    def __str__(self):
        return f"{self.id}, {self.name}"

class User(AbstractUser):
    team        = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True, default=1)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.username

    # def has_perm(self, perm, obj=None):
    #     return True

    # def has_module_perms(self, app_label):
    #     return True

