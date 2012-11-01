# -*- coding: UTF-8 -*-

class Badge(object):
    slug = ""
    title = ""
    description = ""
    allow_multiple = False
    
    def should_award(self, user, **kwargs):
        return False
        
    def check_achievement(self, user, **kwargs):
        from gamified.badges.models import BadgeAchievement
        if should_award(user, **kwargs):
            if not BadgeAchievement.objects.filter(
                user=user,
                slug=self.slug,
                ).count() or self.allow_multiple:
                achievement = BadgeAchievement.objects.create(
                    user=user,
                    slug=self.slug,
                    )

def get_badge_registry():
    from django.conf import settings
    from django.core.exceptions import ImproperlyConfigured
    from django.utils.datastructures import SortedDict
    from django.utils.importlib import import_module
    badge_registry = SortedDict()
    for path in settings.GAMIFIED_BADGES:
        i = path.rfind('.')
        module, attr = path[:i], path[i+1:]
        try:
            mod = import_module(module)
        except ImportError, e:
            raise ImproperlyConfigured('Error importing gamified badge module %s: "%s"' % (module, e))
        try:
            badge_class = getattr(mod, attr)
        except AttributeError:
            raise ImproperlyConfigured('Module "%s" does not define a "%s" callable request processor' % (module, attr))
        badge = badge_class()
        badge_registry[badge.slug] = badge
    return badge_registry

badge_registry = get_badge_registry()

def check_achievement(slug, user, **kwargs):
    badge_registry[slug].check_achievement(user, **kwargs)