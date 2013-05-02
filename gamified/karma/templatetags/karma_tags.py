# -*- coding: UTF-8 -*-

from django import template
from django.db import models

from gamified.karma.models import Karma, KarmaChange

register = template.Library()

# FILTERS

@register.filter
def get_karma_points(user):
    try:
        karma = Karma.objects.get(user=user)
    except Karma.DoesNotExist:
        karma = Karma()
    return karma.points

# TAGS

@register.inclusion_tag("gamified/karma/includes/user_karma_changes.html", takes_context=True)
def user_karma_changes(context, user):
    return {
        'karma_changes': KarmaChange.objects.filter(
            karma__user=user,
            ).distinct()
        }

