# -*- coding: UTF-8 -*-

from django.utils.translation import ugettext_lazy as _

from gamified.badges.base import Badge

class VIPBadge(Badge):
    slug = "vip"
    title = _("VIP")
    description = _("Only very important people get this badge.")
    
class MemberBadge(Badge):
    slug = "member"
    title = _("Member")
    description = _("You get this badge when you register to the website")
    
    def should_award(self, user):
        return user.is_active
    
