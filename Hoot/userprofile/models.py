from django.conf import settings
from django.db import models

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile"
    )
    profile_picture = models.ImageField(
        upload_to="profile_pictures/",
        default="default_profile.jpg",
        blank=True,
        null=True,
    )
    bio = models.TextField(default="This is a bio", blank=True, null=True)
