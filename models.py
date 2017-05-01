from __future__ import unicode_literals

from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

try:
    from django.contrib.auth.backends import get_user_model
    UserModel = get_user_model()

except Exception as e:
    from django.contrib.auth.models import User
    UserModel = User


class ProfileBasicInformation(models.Model):
    class Meta:
        abstract = True

    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField(default=0)
    biography = models.TextField()
    image = models.FileField(blank=True,
                             null=True)


class ProfileContactInformation(models.Model):
    class Meta:
        abstract = True

    telephone = models.CharField(max_length=15,
                                 blank=True,
                                 null=True)
    mobile = PhoneNumberField(
        max_length=15,
        blank=True,
        null=True,
        help_text='eg +254712345678'
    )
    website = models.URLField(blank=True)
    SKYPE = models.CharField(max_length=255,
                             blank=True,
                             null=True,
                             help_text='provide your username')
    FACEBOOK = models.CharField(max_length=255,
                                blank=True,
                                null=True,
                                help_text='provide your username')
    TWITTER = models.CharField(max_length=255,
                               blank=True,
                               null=True,
                               help_text='provide your username')


class ProfileLocationInformation(models.Model):
    class Meta:
        abstract = True

    country = models.CharField(max_length=100,
                               blank=True,
                               null=True)
    city = models.CharField(max_length=100,
                            blank=True,
                            null=True)
    town = models.CharField(max_length=100,
                            blank=True,
                            null=True)
    postal_code = models.CharField(max_length=100,
                                   blank=True,
                                   null=True,
                                   default="Not Provided")


class UserProfile(models.Model):
    user = models.OneToOneField(UserModel)
    slug = models.SlugField(unique=True, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'UserProfile for %s' % self.user.username.capitalize()


class UserProfileBasic(ProfileBasicInformation):
    profile = models.OneToOneField(UserProfile, related_name='userprofile_basic')

    def __str__(self):
        return 'Basic Informaion for %s' % self.profile.user.username


class UserProfileContact(ProfileContactInformation):
    profile = models.OneToOneField(UserProfile, related_name='userprofile_contact')

    def __str__(self):
        return 'Contact Informaion for %s' % self.profile.user.username


class UserProfileLocation(ProfileContactInformation):
    profile = models.OneToOneField(UserProfile, related_name='userprofile_location')

    def __str__(self):
        return 'Location Informaion for %s' % self.profile.user.username

