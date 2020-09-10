# your django admin
from django.contrib import admin

from ib_utility_tools.models import Checklist, ChecklistItem, Timer


class ChecklistItemInline(admin.TabularInline):
    model = ChecklistItem
    extra = 0


class ChecklistAdmin(admin.ModelAdmin):
    list_display = ("checklist_id", "entity_id", "entity_type")
    list_filter = ["entity_type"]
    inlines = [ChecklistItemInline]


class ChecklistItemAdmin(admin.ModelAdmin):
    list_display = ("checklist_item_id", "text", "is_checked", "checklist_id")
    list_filter = ["checklist_id"]


class TimerAdmin(admin.ModelAdmin):
    list_display = (
        "entity_id", "entity_type", "duration_in_seconds", "is_running")
    list_filter = ["entity_type"]


admin.site.register(Checklist, ChecklistAdmin)
admin.site.register(ChecklistItem, ChecklistItemAdmin)
admin.site.register(Timer, TimerAdmin)
