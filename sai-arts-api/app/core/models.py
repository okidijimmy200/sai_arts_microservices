from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin

class UserManager(BaseUserManager):

    # extra_fields, pass extra functions and add it to user
    def create_user(self, email, password=None, **extra_fields):
        '''creates and saves a new user'''
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        '''creates and saves a new superuser'''
        user= self.create_user(email, password)
        user.is_staff  = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    '''custom user model that supports using email'''
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff =  models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def has_module_perms(self, user):
        return self.is_superuser
    