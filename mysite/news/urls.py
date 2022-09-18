from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('test/', test),
    path('for_anna/', for_anna),
]
