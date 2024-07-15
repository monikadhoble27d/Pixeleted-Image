# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.process_image_api, name='process_image_api'),
]
