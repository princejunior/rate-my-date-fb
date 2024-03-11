from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, UserManager,AbstractBaseUser, PermissionsMixin
from django.utils import timezone
import uuid


class Person(models.Model):
    id = models.CharField(primary_key=True, max_length=100)  # Assuming Firestore document IDs are less than 100 characters
    # Model for storing information about a person
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    instagram = models.CharField(max_length=100, blank=True, null=True)  # Optional Instagram handle
    joined_date = models.DateField(null=True)  # Date when the person joined the platform

class Post(models.Model):
    # Model for storing posts associated with a person
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  # User who created the post
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)  # Person associated with the post
    content = models.TextField(default='')  # Content of the post
    how_met = models.CharField(max_length=100, null=True)  # How the user met the person
    agree = models.IntegerField(default=0)  # Number of agreements on the post
    disagree = models.IntegerField(default=0)  # Number of disagreements on the post
    created_at = models.DateTimeField(default=timezone.now, editable=False, blank=True)  # Date and time when the post was created

    def save(self, *args, **kwargs):
        # Override save method to set created_at when the post is first saved
        if not self.pk:
            self.created_at = timezone.now()
        return super(Post, self).save(*args, **kwargs)

class Review(models.Model):
    person_id = models.CharField(max_length=100)  # Assuming person_id is a string
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField(blank=True)  # Optional comment field
    time_created = models.DateTimeField(auto_now_add=True)  # Automatically set to current date and time
    how_met = models.CharField(max_length=100)

    def __str__(self):
        return f"Review by {self.user.username} for person {self.person_id}"

    
    
class Comment(models.Model):
    # Model for storing comments on posts
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)  # Post that the comment belongs to
    comment_date_created = models.DateField(null=True)  # Date when the comment was created
    agree = models.CharField(max_length=255)  # Agree on the comment
    disagree = models.IntegerField(null=True)  # Disagree on the comment







# AUTHENTIACTION
class CustomUserManager(UserManager) :
    def _create_user(self, email,password, **extra_fields):
        if not email:
            raise ValueError( "you have not provided a valid e-mail")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email=None,password=None, **extra_fields) :
        extra_fields.setdefault('is_staff',False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email,password, **extra_fields)
    
    def create_superuser(self, email=None,password=None, **extra_fields) :
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email,password, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin) :
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    email = models.EmailField(blank=True, default='', unique=True)
    # name = models.CharField(max_length=255, blank=True, default='')
    # password = 
    
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD= 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        
    # def get_full_name(self):
    #     return self.name
        
    # def get_short_name(self):
    #     return self.name or self.email.split('@')[0]
    def get_short_name(self):
        return self.email.split('@')[0]