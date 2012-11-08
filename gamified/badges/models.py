# -*- coding: UTF-8 -*-

from datetime import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _

def badge_choices():
    from registry import badge_registry
    for badge_slug, badge in badge_registry.items():
        yield (badge_slug, badge.title)

class BadgeAchievement(models.Model):
    user = models.ForeignKey("auth.User")
    creation_date = models.DateTimeField(default=datetime.now)
    badge = models.SlugField(max_length=255, choices=badge_choices())
    
    class Meta:
        verbose_name = _("Badge Achievement")
        verbose_name_plural = _("Badge Achievements")
        db_table = "gamified_badgeachievement"
        
    def __unicode__(self):
        return _("%(badge)s for %(username)s") % {
            'badge': self.get_badge_display(),
            'username': self.user.username,
            }
            
    def get_badge(self):
        from registry import badge_registry
        return badge_registry[self.badge]
