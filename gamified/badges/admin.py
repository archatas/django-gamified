# -*- coding: UTF-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from models import BadgeAchievement

class BadgeAchievementAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ("creation_date", "user", "badge", )
    list_filter = ("creation_date", "badge", )
    ordering = ("-creation_date", )


admin.site.register(BadgeAchievement, BadgeAchievementAdmin)

