from django.urls import path
from .views import *

urlpatterns = [
    path('app/', index, name='index'),
    path('', appointmentForm, name='appointment'),
    path('info/', info, name='info'),
    path('news/', news, name='news'),
]
