from django import template
from django.core.urlresolvers import reverse


register = template.Library()


@register.inclusion_tag(
    'user_profile/tags/nav/update_link.html',
    takes_context=True
)
def update_link(context):
    request = context['request']
    user = request.user
    link = reverse('user_profile:userprofile_update', kwargs={'slug': user, })
    return {
        'link': link,
    }


@register.inclusion_tag(
    'user_profile/tags/nav/profile_link.html',
    takes_context=True
)
def profile_link(context):
    request = context['request']
    user = request.user
    link = reverse('user_profile:userprofile_detail', kwargs={'slug': user, })
    return {
        'link': link,
    }