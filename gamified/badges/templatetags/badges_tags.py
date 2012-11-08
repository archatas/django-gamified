# -*- coding: UTF-8 -*-

from django import template
from django.db import models

from gamified.badges.registry import badge_registry
from gamified.badges.models import BadgeAchievement

register = template.Library()

# FILTERS

@register.filter
def get_badge(slug):
    return badge_registry[slug]

# TAGS

@register.inclusion_tag("gamified/badges/available_badges.html", takes_context=True)
def available_badges(context):
    return {
        'badges': badge_registry.values()
        }

@register.inclusion_tag("gamified/badges/user_badges.html", takes_context=True)
def user_badges(context, user):
    return {
        'achievements': BadgeAchievement.objects.filter(
            user=user,
            ).values("badge").annotate(models.Count('badge'))
        }
        
