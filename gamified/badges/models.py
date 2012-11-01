# -*- coding: UTF-8 -*-

from datetime import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _

class BadgeAchievement(models.Model):
    user = models.ForeignKey("auth.User")
    creation_date = models.DateTimeField(default=datetime.now)
    slug = models.SlugField(max_length=255)
    
    class Meta:
        verbose_name = _("Badge Achievement")
        verbose_name_plural = _("Badge Achievements")
        db_table = "gamified_badgeachievement"
        
    def __unicode__(self):
        return _("%(slug)s for %(username)s") % {
            'slug': self.slug,
            'uername': self.user.username,
            }
