from django.db import models

from ib_boards.models import Board


class UserStarredBoard(models.Model):
    user_id = models.CharField(max_length=100)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user_id', 'board')
