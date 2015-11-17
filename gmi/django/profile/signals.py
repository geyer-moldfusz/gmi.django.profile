from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from gmi.django.profile.models import Profile


@receiver(post_save, sender=User)
def ensure_profile(sender, instance, **kwargs):
    try:
        instance.profile
    except Profile.DoesNotExist:
        instance.profile = Profile.objects.create(about='', user=instance)
