# your django admin
from django.contrib import admin

from ib_boards.models import Board, Column, ColumnPermission

admin.site.register(Board)
admin.site.register(Column)
admin.site.register(ColumnPermission)
