from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, email, team_id, password=None):
        if not username:
            raise ValueError("Username is required!")
        if not email:
            raise ValueError("Please provide an active email")

        user = self.model(
            username = username,
            email = self.normalize_email(email),
            team_id = team_id
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,  username, email, team_id, password=None):
        user = self.create_user(
            username=username,
            email=email,
            team_id=team_id,
            password=password
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
    
        user.save(using=self._db)
        return user



            


class User(AbstractBaseUser):
    username     = models.CharField(verbose_name="Username", max_length=50, unique=True)
    email        = models.EmailField(verbose_name="Email", max_length=100)
    password     = models.CharField(verbose_name="Password", max_length=1000)
    team_id      = models.PositiveIntegerField(default=0)
    data_joined  = models.DateTimeField(verbose_name="Date joined", default=timezone.now())
    last_login   = models.DateTimeField(verbose_name="Last login", default=timezone.now())
    is_admin     = models.BooleanField(default=False)
    is_active    = models.BooleanField(default=False) 
    is_staff     = models.BooleanField(default=False) 
    is_superuser = models.BooleanField(default=False) 

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'team_id']

    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True