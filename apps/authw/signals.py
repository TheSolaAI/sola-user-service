from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User, UserSettings


@receiver(post_save, sender=User)
def user_saved(sender, instance, created, **kwargs):
    try:
        if created:
            UserSettings.objects.get_or_create(user=instance)

    except Exception as e:
        instance.delete()
        raise e
