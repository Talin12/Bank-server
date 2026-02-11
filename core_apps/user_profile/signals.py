from typing import Any, Type
from django.db.models.base import Model

from django.db.models.signals import post_save
from django.dispatch import receiver
from loguru import logger
from config.settings.base import AUTH_USER_MODEL
from core_apps.user_profile.models import Profile

@receiver(post_save, sender=AUTH_USER_MODEL)
def create_user_profile(sender: Type[Model], instance: Model, created: bool, **kwargs: Any) -> None:
    """
    Create a profile for newly registered users.
    Only runs on user creation, not on every save.
    """
    if created:
        # Create profile without triggering full_clean validation
        # We'll let users update their profile later with proper validation
        Profile.objects.create(user=instance)
        logger.info(f"Profile created for {instance.first_name} {instance.last_name}")

# REMOVED the save_user_profile signal - it was causing double saves and validation errors
# The profile will be saved properly when users update it through the API