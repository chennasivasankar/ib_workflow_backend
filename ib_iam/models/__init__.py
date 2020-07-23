from ib_iam.models.role import Role
from ib_iam.models.company import Company
from ib_iam.models.team import Team, TeamMember
from ib_iam.models.user import UserRole, UserTeam, UserDetails
__all__ = ["Role", "Team", "Company", "UserTeam", "UserRole", "UserDetails", "TeamMember"]

# class DummyModel(AbstractDateTimeModel):
#     """
#     Model to store key value pair
#     Attributes:
#         :var key: String field which will be unique
#         :var value: String field which will be of 128 char length
#     """
#     key = models.CharField(max_length=128, unique=True)
#     value = models.CharField(max_length=128)
#
#     class Meta(object):
#         app_label = 'sample_app'
#
#     def __str__(self):
#         return "<DummyModel: {key}-{value}>".format(key=self.key,
#                                                     value=self.value)
#
