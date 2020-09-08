# your django admin
from django.contrib import admin

from ib_boards.models import Board, Column, ColumnPermission, FieldOrder, FieldDisplayStatus

admin.site.register(Board)
admin.site.register(ColumnPermission)


class ColumnAdmin(admin.ModelAdmin):
    list_display = ('column_id', 'name', 'board_id', 'task_selection_config')
    list_editable = 'task_selection_config',


admin.site.register(Column, ColumnAdmin)
admin.site.register(FieldDisplayStatus)
admin.site.register(FieldOrder)
