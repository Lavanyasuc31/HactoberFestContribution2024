from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from .models import Profile, Job
from .tasks import check_job_match_and_notify_users

@receiver(post_save, sender=User)       
def user_postsave(sender, instance, created, **kwargs):
    print("POSTSAVE")
    user = instance
    
    # add profile if user is created
    print("OK1")
    if created:
        print("OK2")
        Profile.objects.create(
            user = user,
        )


@receiver(post_save, sender=Job)
def job_post_save(sender, instance, created, **kwargs):
    print("signal invloked")
    if created:  # Check if a new job was created
        check_job_match_and_notify_users.apply_async(args=[instance.id])  # Call Celery task

