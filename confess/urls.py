from django.urls import path
from .views import register,home,create_confess,my_confession,all_confession
urlpatterns = [
path('register/', register, name='register'), 
path('home/',home,name='home'),
path('confess/',create_confess,name='create_confess'),
path('myconfession/',my_confession,name='my_confession'),
path('allconfession/',all_confession,name='all_confession'),
path('',home,name='initial')
]