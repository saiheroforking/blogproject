from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import RegisterForm, UserRole


@receiver(post_save, sender=RegisterForm)
def assign_default_role(sender, instance, created, **kwargs):
    if created:
        if not instance.role:
            instance.role = UserRole.READER
            instance.save()
