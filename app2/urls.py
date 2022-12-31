from django.urls import path
from app2.views import *


app_name='dad'

urlpatterns=[
    path('lucky/',lucky,name='lucky'),
]
    
