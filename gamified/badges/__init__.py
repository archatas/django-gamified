# -*- coding: UTF-8 -*-

from registry import badge_registry

def check_achievement(slug, user, **kwargs):
    badge_registry[slug].check_achievement(user, **kwargs)