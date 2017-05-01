# user_profile
is an app that allows lazy django developers to hook it to there django projects.

this app creates a user_profile instance automatically the user is added to the default django ```User``` model.

## installation
1. install required dependancies in the ```requirements.txt``` file.

2. add ```user_profile``` to ```INSTALLED_APPS```.

3. add ``` url(r'^profile/', include('user_profile.urls')),``` in your main ```urls.py``` file.

4. run ``` python manage.py makemigrations``` then ```python manage.py migrate```.

5. add ```os.path.join(BASE_DIR, 'user_profile/cdn/staticfiles')``` to your STATICFILES_DIRS such that
   it looks like
   ```python
       STATICFILES_DIRS = [
           ...
           os.path.join(BASE_DIR, 'user_profile/cdn/staticfiles'),
           ...
       ]
   ```

6. for styling add ```<link href="{% static 'user_profile/css/profile.css' %}" rel="stylesheet">``` to your ```base.html```

7. the app provides ```{% update_link %}``` and ```{% profile_link %}``` tags which is accessed by adding ```{% load navigation_links %}``` at the top of the ```html file```.





