# -*- coding: UTF-8 -*-

from datetime import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _

class Karma(models.Model):
    user = models.OneToOneField("auth.User")
    points = models.IntegerField(default=0)

    class Meta:
        verbose_name = _("Karma")
        verbose_name_plural = _("Karmas")
        db_table = "gamified_karma"
    
    def __unicode__(self):
        return _("%(username)s: %(points)d") % {
            'username': self.user.username,
            'points': self.points,
            }

class KarmaChange(models.Model):
    karma = models.ForeignKey(Karma)
    creation_date = models.DateTimeField(default=datetime.now)
    delta = models.SmallIntegerField()
    reason = models.TextField(blank=True)
    
    class Meta:
        verbose_name = _("Karma Change")
        verbose_name_plural = _("Karma Changes")
        db_table = "gamified_karmachange"
        
    def __unicode__(self):
        return _("%(username)s: %(delta)+d") % {
            'username': self.karma.user.username,
            'delta': self.delta,
            }

    def save(self, *args, **kwargs):
        is_new = not self.pk
        super(KarmaChange, self).save(*args, **kwargs)
        if is_new:
            self.karma.points += self.delta
            self.karma.save()
