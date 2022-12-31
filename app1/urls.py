from django.urls import path
from app1.views import *


app_name='mom'

urlpatterns=[
    path('sasank/',sasank,name='sasank'),
]