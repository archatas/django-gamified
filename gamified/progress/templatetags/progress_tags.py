# -*- coding: UTF-8 -*-
from django import template

register = template.Library()

@register.inclusion_tag('gamified/progress/includes/progress.html')
def show_progress(value, str_out, str_of, max_value):
    persentage = int(float(value) / max_value * 100)
    if persentage < 1:
        persentage = 1
    return {
        'value': value,
        'max_value': max_value,
        'persentage': persentage,
        }

