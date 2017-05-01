from django.conf.urls import url

from . import views

app_name = 'user_profile'


urlpatterns = [
    url(r'^(?P<slug>[A-Za-z0-9_-]+)$', views.UserProfileDetailView.as_view(), name='userprofile_detail'),
    url(r'^(?P<slug>[A-Za-z0-9_-]+)/update/$', views.UpdateUserProfileView.as_view(), name='userprofile_update'),
]