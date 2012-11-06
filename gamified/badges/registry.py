# -*- coding: UTF-8 -*-
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.datastructures import SortedDict
from django.utils.importlib import import_module

def get_badge_registry():
    if not hasattr(get_badge_registry, "_cache"):
        badge_registry = SortedDict()
        for path in getattr(settings, "GAMIFIED_BADGES", []):
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
        get_badge_registry._cache = badge_registry
    return get_badge_registry._cache

badge_registry = get_badge_registry()

