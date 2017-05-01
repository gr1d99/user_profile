from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views.generic import DetailView, UpdateView, TemplateView
from .forms import UserProfileForm
from .models import UserProfile
from permissions import ProfileOwnerMixin

from braces.views import LoginRequiredMixin


class UserProfileDetailView(LoginRequiredMixin, ProfileOwnerMixin, DetailView):
    model = UserProfile
    template_name = 'user_profile/userprofile_detail.html'


class UpdateUserProfileView(LoginRequiredMixin, ProfileOwnerMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'user_profile/userprofile_update.html'

    def form_valid(self, form):
        return super(UpdateUserProfileView, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(UpdateUserProfileView, self).get_form_kwargs()
        kwargs.update(
            instance={
                'userprofile': self.object,
                'basic': self.object.userprofile_basic,
                'contact': self.object.userprofile_contact,
                'location': self.object.userprofile_location,
            }
        )
        return kwargs

    def get_success_url(self):
        messages.success(self.request, 'Profile Successfully Updated')
        return reverse('user_profile:userprofile_detail', kwargs={'slug': self.request.user, })

