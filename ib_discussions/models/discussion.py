import datetime
import uuid

from django.db import models

from ib_discussions.models.discussion_set import DiscussionSet


def generate_uuid():
    return uuid.uuid4()


def get_datetime_now():
    return datetime.datetime.now()


class Discussion(models.Model):
    id = models.UUIDField(primary_key=True, default=generate_uuid,
                          editable=False)
    discussion_set = models.ForeignKey(
        DiscussionSet, on_delete=models.CASCADE
    )
    user_id = models.UUIDField(editable=False)
    description = models.TextField()
    title = models.TextField()
    created_at = models.DateTimeField(default=get_datetime_now)
    is_clarified = models.BooleanField(default=False)
