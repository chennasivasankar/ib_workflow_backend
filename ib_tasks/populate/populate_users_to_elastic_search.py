"""
Created on: 08/08/20
Author: Pavankumar Pamuru

"""


class UserDetailsToElasticSearch:

    @staticmethod
    def push_user_details_to_elasticsearch():
        from ib_iam.models import UserDetails
        user_objects = UserDetails.objects.all()

        for user_object in user_objects:
            from ib_tasks.documents.elastic_task import User
            user = User(user_id=user_object.user_id, name=user_object.name)
            user.save()

