#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 16:41:02 2022

@author: apple
"""
from django.conf.urls import url
from django.urls import path 
from rango import views
app_name = 'rango'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path("index/", views.index, name='index'),
    path('category/<slug:category_name_slug>/',
         views.show_category, name='show_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
    path('add_category/', views.add_category, name='add_category'),
   # path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page'),
]