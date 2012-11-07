# -*- coding: UTF-8 -*-

class Badge(object):
    slug = ""
    title = ""
    description = ""
    allow_multiple = False
    
    def should_award(self, user, *args, **kwargs):
        return False
        
    def check_achievement(self, user, *args, **kwargs):
        from gamified.badges.models import BadgeAchievement
        if self.should_award(user, *args, **kwargs):
            if not BadgeAchievement.objects.filter(
                user=user,
                badge=self.slug,
                ).count() or self.allow_multiple:
                achievement = BadgeAchievement.objects.create(
                    user=user,
                    badge=self.slug,
                    )
