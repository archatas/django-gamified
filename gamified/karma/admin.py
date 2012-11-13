# -*- coding: UTF-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from models import Karma, KarmaChange

class KarmaAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ("user", "points", )
    search_fields = ("user__first_name", "user__last_name", "user__username", "user__email")
    ordering = ("user__username", )

class KarmaChangeAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ("karma", "creation_date", "delta", "reason")
    list_filter = ("creation_date", )
    search_fields = ("karma__user__first_name", "karma__user__last_name", "karma__user__username", "karma__user__email")
    ordering = ("-creation_date", )

admin.site.register(Karma, KarmaAdmin)
admin.site.register(KarmaChange, KarmaChangeAdmin)
