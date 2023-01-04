from django.urls import include, path
from django.shortcuts import render

urlpatterns = [
    path("", render("hello there")),
]
