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
