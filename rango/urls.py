#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 16:41:02 2022

@author: apple
"""

from django.urls import path 
from rango import views
app_name = 'rango'
urlpatterns = [
    path('', views.index, name='index'),
]
