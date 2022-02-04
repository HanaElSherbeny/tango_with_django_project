#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 18:10:56 2022

@author: apple
"""

from django import template 
from rango.models import Category

register=template.Library()

@register.inclusion_tag('rango/categories.html') 
def get_category_list(current_category=None): 
    return {'categories': Category.objects.all(), 'current_category': current_category}
