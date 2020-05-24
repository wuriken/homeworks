from django.db.models.signals import pre_save
from django.dispatch import receiver

from teachers.models import Teacher


@receiver(pre_save, sender=Teacher)
def student_pre_save(sender, instance, **kwargs):
    instance.first_name = str(instance.first_name).lower().capitalize()
    instance.last_name = str(instance.last_name).lower().capitalize()
