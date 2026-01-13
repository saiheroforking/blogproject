from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Comment, Notification

@receiver(post_save, sender=Comment)
def notify_post_author(sender, instance, created, **kwargs):
    if created:
        post = instance.post
        author = post.author
        commenter = instance.user

        if author != commenter:
            Notification.objects.create(
                recipient=author,
                message=f"{commenter.username} commented on your post: '{post.title}'"
            )
