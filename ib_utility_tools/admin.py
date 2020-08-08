# your django admin
from django.contrib import admin

from ib_utility_tools.models import Checklist, ChecklistItem, Timer

admin.site.register(Checklist)
admin.site.register(ChecklistItem)
admin.site.register(Timer)
