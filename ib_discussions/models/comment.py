import uuid
from datetime import datetime

from django.db import models

from ib_discussions.models import Discussion
from ib_discussions.models.multi_media import MultiMedia


def generate_uuid():
    return uuid.uuid4()


def get_datetime_now():
    return datetime.now()


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=generate_uuid,
                          editable=False)
    user_id = models.CharField(max_length=40)
    discussion = models.ForeignKey(
        Discussion, related_name="comments", on_delete=models.CASCADE,
        null=True, default=None)
    parent_comment = models.ForeignKey(
        'self', related_name="replies", on_delete=models.CASCADE,
        null=True, default=None)
    created_at = models.DateTimeField(default=get_datetime_now)
    content = models.TextField()


class CommentWithMultiMedia(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    multi_media = models.ForeignKey(MultiMedia, on_delete=models.CASCADE)


class CommentWithMentionUserId(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    mention_user_id = models.CharField(max_length=40)
