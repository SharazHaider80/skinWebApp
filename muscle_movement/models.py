from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import UserManager
from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone

class CustomUserManager(BaseUserManager):

    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)

class User(AbstractBaseUser):
    username = models.CharField(db_column='username', max_length=100, blank=False, unique=True)
    first_name = models.CharField(db_column='first_name', max_length=100, blank=True)
    last_name = models.CharField(db_column='last_name', max_length=100, blank=True)
    full_name = models.CharField(db_column='full_Name', max_length=100)
    email = models.EmailField(db_column='email', blank=True)
    is_active = models.BooleanField(db_column='is_active', blank=True)
    is_superuser = models.BooleanField(db_column='is_superuser', blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True)
    admin = models.ForeignKey('User', null=True, db_column='admin', on_delete=CASCADE)
    USERNAME_FIELD = 'username'

    objects = CustomUserManager()

    def get_user_admin(self):
        return self.admin if self.admin else self

    def get_user_full_name(self):
        return f'{self.first_name} {self.last_name}' if self.first_name or self.last_name else self.full_name

    class Meta:
        db_table = 'user'
