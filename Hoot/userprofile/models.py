from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    bio = models.TextField(blank=True, null=True)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
