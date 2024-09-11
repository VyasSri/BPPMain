from django.shortcuts import render
from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.home),
    path('glance/', views.glance),
    path('demo/', views.demo_view),
    path('FF/', views.FF),
    path('NF/', views.NF),
    path('BF/', views.BF),
    path('WF/', views.WF),
    path('applications/', views.applications),
]