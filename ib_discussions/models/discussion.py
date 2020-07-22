import uuid

from django.db import models

from ib_discussions.models.discussion_set import DiscussionSet


def generate_uuid():
    return uuid.uuid4()


class Discussion(models.Model):
    id = models.UUIDField(primary_key=True, default=generate_uuid,
                          editable=False)
    discussion_set = models.ForeignKey(
        DiscussionSet, on_delete=models.CASCADE
    )
    user_id = models.CharField(max_length=100)
    description = models.TextField()
    title = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    is_clarified = models.BooleanField(default=False)

