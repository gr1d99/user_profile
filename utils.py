from .models import UserProfile


def get_userprofile_by_slug(slug):
    try:
        profile = UserProfile.objects.get(slug=slug)
        return profile

    except UserProfile.DoesNotExist:
        return False