# coding: utf-8
from django.urls import path
from shd.views import tagslist, element



urlpatterns = [
    path(r'tags/list', tagslist, name='tagslist'),
    path(r'element', element, name="element")

]