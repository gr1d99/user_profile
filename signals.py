from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save, pre_delete
from django.dispatch import receiver
from .models import UserProfile, UserProfileBasic, UserProfileContact, UserProfileLocation


def create_userprofile(sender, instance, created, **kwargs):
    if created:
        profile = UserProfile()
        profile.user = instance
        profile.save()


def create_userprofile_slug(sender, instance, **kwargs):
    slug = instance.user.username
    instance.slug = slug


pre_save.connect(create_userprofile_slug, sender=UserProfile)


def instantiate_userprofile_other_models(sender, instance, created, **kwargs):
    if created:
        basic = UserProfileBasic()
        contact = UserProfileContact()
        location = UserProfileLocation()
        basic.profile = instance
        contact.profile = instance
        location.profile = instance
        basic.save()
        contact.save()
        location.save()


post_save.connect(create_userprofile, sender=User)
post_save.connect(instantiate_userprofile_other_models, sender=UserProfile)
