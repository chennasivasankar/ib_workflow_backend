import factory

from ib_iam.interactors.presenter_interfaces.dtos import \
    DiscussionIdWithEditableStatusDTO


class DiscussionIdWithEditableStatusDTOFactory(factory.Factory):
    class Meta:
        model = DiscussionIdWithEditableStatusDTO

    discussion_id = factory.Faker("uuid4")
    is_editable = factory.Iterator([True, False])
