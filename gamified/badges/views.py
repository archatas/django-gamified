# -*- coding: UTF-8 -*-

from django.db import models
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

from gamified.badges.registry import badge_registry
from gamified.badges.models import BadgeAchievement

def badge_list(request):
    from gamified.badges.registry import badge_registry
    if request.user.is_authenticated():
        for achievement in BadgeAchievement.objects.filter(
            user=request.user,
            ).values("badge").annotate(models.Count('badge')):
            badge_registry[achievement['badge']].count = achievement['badge__count']
    badges = badge_registry.values()
    return render(
        request,
        "gamified/badges/badge_list.html",
        {'badges': badges},
        )
    
def user_badges(request, username):
    user = get_object_or_404(User, username=username)
    for achievement in BadgeAchievement.objects.filter(
        user=user,
        ).values("badge").annotate(models.Count('badge')):
        badge_registry[achievement['badge']].count = achievement['badge__count']
    badges = badge_registry.values()
    return render(
        request,
        "gamified/badges/user_badges.html",
        {'user': user, 'badges': badges},
        )
    
