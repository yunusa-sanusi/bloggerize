from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models

from autoslug import AutoSlugField


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        upload_to='images/profile-pictures', null=True, blank=True)
    bio = models.TextField()
    age = models.IntegerField(default=18, validators=[
                              MinValueValidator(18)])
    slug = AutoSlugField(unique=True, always_update=True, populate_from='user')

    @property
    def get_profile_image(self):
        try:
            image = self.profile_picture.image_url
        except:
            image = ''
        return image

    def __str__(self):
        return self.user
