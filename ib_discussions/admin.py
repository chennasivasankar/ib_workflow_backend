# your django admin
from django.contrib import admin

from ib_discussions.models import Discussion, DiscussionSet, Comment


class DiscussionAdmin(admin.ModelAdmin):
    list_display = ("user_id", "description", "title", "is_clarified")
    search_fields = ["user_id"]
    list_filter = ["is_clarified"]


class DiscussionInline(admin.TabularInline):
    model = Discussion
    extra = 0


class DiscussionSetAdmin(admin.ModelAdmin):
    list_display = ("id", "entity_id", "entity_type")
    list_filter = ["entity_type"]
    search_fields = ["entity_id"]
    inlines = [DiscussionInline]


class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "discussion_id", "content")
    list_filter = ["discussion_id"]


admin.site.register(Discussion, DiscussionAdmin)
admin.site.register(DiscussionSet, DiscussionSetAdmin)
admin.site.register(Comment, CommentAdmin)
