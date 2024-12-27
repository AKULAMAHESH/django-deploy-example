from django.urls import path
from .views import *

app_name='app'

urlpatterns=[
    path('home/',home, name='home'),
    path('courses/',courses, name='courses'),
    path('bootcamp/',bootcamp, name='bootcamp'),
    

]