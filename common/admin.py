from django.contrib import admin

from common.models import Lem
from common.models import Meaning


class MeaningInline(admin.TabularInline):
    model = Meaning

class LemAdmin(admin.ModelAdmin):
    inlines = [
        MeaningInline,
    ]

admin.site.register(Lem, LemAdmin)
