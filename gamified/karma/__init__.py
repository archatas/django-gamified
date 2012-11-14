# -*- coding: UTF-8 -*-

def change_karma(user, delta, reason=""):
    from models import Karma, KarmaChange
    karma, created = Karma.objects.get_or_create(user=user)
    change = KarmaChange(karma=karma, delta=delta, reason=reason)
    change.save()