from django.contrib import admin

from common.models import Lem
from common.models import Meaning


class MeaningInline(admin.TabularInline):
    model = Meaning


class LemAdmin(admin.ModelAdmin):
    list_display = ('graphs', 'pinyin')
    inlines = [
        MeaningInline,
    ]


class MeaningAdmin(admin.ModelAdmin):
    pass

admin.site.register(Lem, LemAdmin)
admin.site.register(Meaning, MeaningAdmin)
