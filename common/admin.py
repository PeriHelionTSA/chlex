from django.contrib import admin

from common.models import Lem


class LemAdmin(admin.ModelAdmin):
    pass

admin.site.register(Lem, LemAdmin)
