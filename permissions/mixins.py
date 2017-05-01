from django.http import Http404
from ..utils import get_userprofile_by_slug


class ProfileOwnerMixin(object):
    def dispatch(self, request, *args, **kwargs):
        user = request.user
        userprofile = get_userprofile_by_slug(kwargs.get('slug', None))

        if user == userprofile.user:
            return super(ProfileOwnerMixin, self).dispatch(request, *args, **kwargs)

        else:
            raise Http404
