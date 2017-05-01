# user_profile
is an app that allows lazy django developers to hook it to there django projects.

this app creates a user_profile instance automatically the user is added to the default django ```User``` model.

django project

## installation
1. install required dependancies in the ```requirements.txt``` file.

2. add ```user_profile``` to ```INSTALLED_APPS```.

3. add ```python url(r'^profile/', include('user_profile.urls')),``` in your main ```urls.py``` file.

4. run ```python python manage.py makemigrations``` then ```python manage.py migrate```.




