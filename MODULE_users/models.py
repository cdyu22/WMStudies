from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class UserManager(BaseUserManager):
    def create_user(self, username, password=None, phone_number=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not username:
            raise ValueError('Users must have a username address')

        user = self.model(
            username= username,
            password=password,
            phone_number=phone_number,
        )

        user.set_password(password)
        user.phone_number = phone_number
        user.save(using=self._db)
        return user

    def create_staffuser(self, username, password,phone_number):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            username,
            password=password,
            phone_number=phone_number,
        )
        user.staff = True
        user.phone_number = phone_number
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password,phone_number):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            username,
            password=password,
            phone_number=phone_number,
        )
        user.phone_number = phone_number
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username = models.CharField(
        verbose_name='Username',
        max_length=32,
        unique=True,
        default="Username"
    )
    USERNAME_FIELD = 'username'
    phone_number = models.CharField(max_length=10,default="Default")
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
    # notice the absence of a "Password field", that is built in.

    REQUIRED_FIELDS = ['phone_number'] # Email & Password are required by default.

    def get_full_name(self):
        # The user is identified by their email address
        return self.username

    def get_short_name(self):
        # The user is identified by their email address
        return self.username

    def __str__(self):              # __unicode__ on Python 2
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def set_phone_number(self,phone_number):
        self.phone_number = phone_number

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active
    
    objects = UserManager()
