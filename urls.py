from django.conf.urls import url

from . import views

app_name = 'user_profile'


urlpatterns = [
    url(r'^$', views.Index.as_view(), name='userprofile_index'),
    url(r'^profile/(?P<slug>[A-Za-z0-9_-]+)$', views.UserProfileDetailView.as_view(), name='userprofile_detail'),
    url(r'^profile/(?P<slug>[A-Za-z0-9_-]+)/update/$', views.UpdateUserProfileView.as_view(), name='userprofile_update'),
]