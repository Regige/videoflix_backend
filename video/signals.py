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
        # convert480p(instance.video_file.path)
        # convert720p(instance.video_file.path)
        # convert1080p(instance.video_file.path)

    
# post_save.connect(video_post_save, sender=Video)




@receiver(post_delete, sender=Video)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes the main file and all related files from the filesystem
    when the corresponding `Video` object is deleted.
    """
    if instance.video_file:
        main_file_path = instance.video_file.path
        if os.path.isfile(main_file_path):
            os.remove(main_file_path)
        
        base_path = main_file_path.rsplit('.', 1)[0]
        for suffix in ['_480p.mp4', '_720p.mp4', '_1080p.mp4']:
            related_file_path = f"{base_path}{suffix}"
            if os.path.isfile(related_file_path):
                os.remove(related_file_path)