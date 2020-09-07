import datetime
import uuid

from django.db import models


def generate_uuid():
    return uuid.uuid4()


def get_datetime_now():
    return datetime.datetime.now()


class ChecklistItem(models.Model):
    checklist_item_id = models.UUIDField(primary_key=True,
                                         default=generate_uuid,
                                         editable=False)
    checklist = models.ForeignKey("Checklist", on_delete=models.CASCADE,
                                  related_name="checklist_items")
    text = models.TextField()
    is_checked = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=get_datetime_now)
