from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
# from .models import (
#     Monitor, MonitorScheduler,
#     Headset, HeadsetScheduler,
#     Speakers, SpeakerScheduler
# )
#
#
# @receiver(pre_save, sender=Monitor)
# def update_scheduler_status_from_monitor(sender, instance, **kwargs):
#     """Обновляет monitorStatus в модели monitorScheduler
#         при обновлении/создании экземпляра в модели Monitor"""
#     try:
#         obj = sender.objects.get(pk=instance.pk)
#     except sender.DoesNotExist:
#         pass
#     else:
#         if obj.status != instance.status:
#             MonitorScheduler.objects.create(
#                 monitor=instance,
#                 status=instance.status,
#                 location=instance.location,
#                 person=instance.person
#             )
#
#
# @receiver(pre_save, sender=Headset)
# def update_scheduler_status_from_headset(sender, instance, **kwargs):
#     """Обновляет headsetStatus в модели HeadsetsScheduler
#         при обновлении/создании экземпляра в модели Headset"""
#     try:
#         obj = sender.objects.get(pk=instance.pk)
#     except sender.DoesNotExist:
#         pass
#     else:
#         if obj.status != instance.status:
#             HeadsetScheduler.objects.create(
#                 headset=instance,
#                 status=instance.status,
#                 location=instance.location,
#                 person=instance.person
#             )
#
#
# @receiver(pre_save, sender=Speakers)
# def update_scheduler_status_from_speaker(sender, instance, **kwargs):
#     """Обновляет speakerStatus в модели SpeakersScheduler
#         при обновлении/создании экземпляра в модели Speaker"""
#     try:
#         obj = sender.objects.get(pk=instance.pk)
#     except sender.DoesNotExist:
#         pass
#     else:
#         if obj.status != instance.status:
#             SpeakerScheduler.objects.create(
#                 speaker=instance,
#                 status=instance.status,
#                 location=instance.location,
#                 person=instance.person
#             )