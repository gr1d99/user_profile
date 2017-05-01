from collections import OrderedDict

from django import forms
from .models import UserProfile, UserProfileBasic, UserProfileContact, UserProfileLocation

from betterforms.multiform import MultiModelForm


class UserProfileBasicForm(forms.ModelForm):
    class Meta:
        model = UserProfileBasic
        exclude = ('profile', )

    def __init__(self, *args, **kwargs):
        super(UserProfileBasicForm, self).__init__(*args, **kwargs)

        for field_name, field_obj in self.fields.items():
            if not field_name == 'image':
                field_obj.widget.attrs.update({'class': 'form-control'})


class UserProfileContactForm(forms.ModelForm):
    class Meta:
        model = UserProfileContact
        exclude = ('profile', )

    def __init__(self, *args, **kwargs):
        super(UserProfileContactForm, self).__init__(*args, **kwargs)

        for field_name, field_obj in self.fields.items():
            field_obj.widget.attrs.update({'class': 'form-control'})


class UserProfileLocationForm(forms.ModelForm):
    class Meta:
        model = UserProfileLocation
        exclude = ('profile', )

    def __init__(self, *args, **kwargs):
        super(UserProfileLocationForm, self).__init__(*args, **kwargs)

        for field_name, field_obj in self.fields.items():
            field_obj.widget.attrs.update({'class': 'form-control'})


class UserProfileForm(MultiModelForm):
    form_classes = OrderedDict((
        ('basic', UserProfileBasicForm),
        ('contact', UserProfileContactForm),
        ('location', UserProfileLocationForm),
    ))
