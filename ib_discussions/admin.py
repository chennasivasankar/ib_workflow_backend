# your django admin
from django.contrib import admin

from ib_discussions.models import Discussion, DiscussionSet, Comment
from ib_discussions.models.comment import CommentWithMultiMedia, \
    CommentWithMentionUserId
from ib_discussions.models.multimedia import MultiMedia


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


class CommentWithMultimediaInline(admin.TabularInline):
    model = CommentWithMultiMedia
    extra = 0


class CommentWithMentionUserIdInline(admin.TabularInline):
    model = CommentWithMentionUserId
    extra = 0


class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "discussion_id", "content")
    list_filter = ["discussion_id"]
    inlines = [CommentWithMentionUserIdInline, CommentWithMultimediaInline]


class MultimediaAdmin(admin.ModelAdmin):
    list_display = ("id", "format_type", "url")


admin.site.register(Discussion, DiscussionAdmin)
admin.site.register(DiscussionSet, DiscussionSetAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(MultiMedia, MultimediaAdmin)
