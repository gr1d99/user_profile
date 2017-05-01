from django.contrib import admin
from .models import UserProfile, UserProfileBasic, UserProfileContact, UserProfileLocation


class AdminUserProfileBasicInline(admin.StackedInline):
    model = UserProfileBasic


class AdminUserProfileContactInline(admin.StackedInline):
    model = UserProfileContact


class AdminUserProfileLocationInline(admin.StackedInline):
    model = UserProfileLocation


class AdminUserProfile(admin.ModelAdmin):
    list_display = ['__str__', 'date_added', 'date_updated']
    inlines = [AdminUserProfileBasicInline, AdminUserProfileContactInline, AdminUserProfileLocationInline]

admin.site.register(UserProfile, AdminUserProfile)

