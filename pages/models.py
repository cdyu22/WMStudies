from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


# # Create your models here.
# class UserManager(BaseUserManager):
#     def create_user(self,password=None,**extra_fields):
        
#         user = self.model( **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#     def create_superuser(self,password):
#         user = self.create_user( password)
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)

#         return user

# class User(AbstractUser):
#     """Custom user model that uses email instead of username"""

#     id = models.CharField(max_length=16,unique=True,blank=False,primary_key=True)
#     password = models.CharField(max_length=16,blank=False)
#     phone = models.CharField(max_length=10,blank=False)
#     email = None
    

#     USERNAME_FIELD = 'id'
#     objects = UserManager()
#     REQUIRED_FIELDS = []

#     def save(self,commit=True):
#         user = super(CustomUserCreationForm,self).save(commit=False)
#         self.phone = self.cleaned_data["phone"]
#         if commit:
#             user.save()
#         return user


#     # USERNAME_FIELD = 'email'

# class Phone(User):
#     objects() = User

# class UserManager(BaseUserManager):
#     def create_user(self,id,password=None):
#         if not id:
#             raise ValueError("Users must have unique username")
        
#         user = self.model()
#         user.set_password(password)
#         user.save(using=self._db)
        
#         print('Checkpoint 1')
#         return user

#     def create_superuser(self,id,password=None):
#         user = self.create_user(id, password=password)
        
#         print('Checkpoint 5')
#         user.staff=True
#         user.admin=True
#         user.save(using=self._db)
#         return user

# class User(AbstractBaseUser):
#     objects = UserManager()
#     id = models.CharField(max_length=16, unique=True, primary_key=True)
#     active = models.BooleanField(default=True)
#     staff = models.BooleanField(default=False) # a admin user; non super-user
#     admin = models.BooleanField(default=False) # a superuser

#     USERNAME_FIELD = 'id'
#     REQUIRED_FIELDS = []

    
#     def get_name(self):
#         return self.id

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not username:
            raise ValueError('Users must have a username address')

        user = self.model(
            username= username,
            password=password,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, username, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            username,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            username,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser):
    username = models.CharField(
        verbose_name='Student Username',
        max_length=32,
        unique=True,
        default="HOLDIN"
    )
    USERNAME_FIELD = 'username'

    # password= models.CharField(max_length=16)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
    # notice the absence of a "Password field", that is built in.

    REQUIRED_FIELDS = [] # Email & Password are required by default.
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

