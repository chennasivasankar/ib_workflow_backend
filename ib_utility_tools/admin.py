# your django admin
from django.contrib import admin

from ib_utility_tools.models import Checklist, ChecklistItem

admin.site.register(Checklist)
admin.site.register(ChecklistItem)
