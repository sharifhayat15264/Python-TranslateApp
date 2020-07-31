from django.contrib import admin
from django.urls import path

# importing views from views..py
from django.conf.urls import url
from . import views

urlpatterns = [
    path('text/', views.text_view, name='text_view'),
    path('file/', views.file_view, name='file_view'),
    path('speech/', views.speech_view, name='speech_view'),
    path('', views.index, name='index'),
]
