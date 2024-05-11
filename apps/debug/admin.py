from django.contrib import admin

from .models import Log


class LogAdmin(admin.ModelAdmin):
    list_display = (
        "text",
        "date_added",
    )
    search_fields = ["text"]


admin.site.register(Log, LogAdmin)
