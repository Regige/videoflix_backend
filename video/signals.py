from .models import Video
from .tasks import convert720p, convert480p, convert1080p
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
import os
import django_rq

@receiver(post_save, sender=Video)
def video_post_save(sender, instance, created, **kwargs):
    if created:
        queue = django_rq.get_queue('default', autocommit=True)
        queue.enqueue(convert720p, instance.video_file.path)
        queue.enqueue(convert480p, instance.video_file.path)
        queue.enqueue(convert1080p, instance.video_file.path)
        # convert720p(instance.video_file.path)
        # convert480p(instance.video_file.path)
        # convert1080p(instance.video_file.path)

    
# post_save.connect(video_post_save, sender=Video)




@receiver(post_delete, sender=Video)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.video_file:
        if os.path.isfile(instance.video_file.path):
            os.remove(instance.video_file.path)