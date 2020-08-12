import datetime
from uuid import UUID

import pytest


@pytest.fixture()
def prepare_discussion_setup(prepare_entity_setup):
    entity_ids = prepare_entity_setup
    from ib_discussions.tests.factories.models import DiscussionSetFactory
    discussion_set_ids = [
        UUID('641bfcc5-e1ea-4231-b482-f7f34fb5c7c4'),
        UUID('94557db1-c123-4e16-a69d-98a6a4850b84'),
        UUID('98ec9bf6-c83c-4f40-9f8c-bd1998b7e452'),
        UUID('e12c2408-fc30-4e55-8f9a-6847d915481e'),
        UUID('f032383d-ea21-4da3-8194-a676be299987')
    ]
    for entity_id, discussion_set_id in list(
            zip(entity_ids, discussion_set_ids)):
        DiscussionSetFactory(entity_id=entity_id, id=discussion_set_id)
    discussion_set_id = "641bfcc5-e1ea-4231-b482-f7f34fb5c7c4"
    discussion_ids = [
        UUID('12f72e4a-aefd-4441-b569-03ca65ab5b62'),
        UUID('50fd3d50-9cc9-482a-8617-3f6ae1bcf7e4'),
        UUID('75e86ce9-337b-4720-9edb-ff9e7d006be1'),
        UUID('78a8927c-6732-4f91-a97f-810214a47663'),
        UUID('7b9486ac-7eb6-424b-bc85-71598d000654'),
        UUID('802bdcf5-efd2-4227-9c42-df8089712d52'),
        UUID('9137b75a-a933-41e1-9150-a494f4a7ef5e'),
        UUID('99fd131e-4e04-4076-afea-94d0640f5fb1'),
        UUID('b2ddc029-ab38-47d4-8d21-781f1add28d4'),
        UUID('c30ad6d3-50fa-4d79-806a-a8d1b1e1be5e'),
        UUID('decca11f-a86b-4256-9ca6-42ecfffa24ac'),
        UUID('f59c5963-271f-4c3c-8761-c801bd2a83db')
    ]
    from ib_discussions.tests.factories.models import DiscussionFactory
    DiscussionFactory.created_at.reset()
    DiscussionFactory.user_id.reset()
    DiscussionFactory.is_clarified.reset()
    for discussion_id in discussion_ids:
        DiscussionFactory(
            discussion_set_id=discussion_set_id,
            id=discussion_id,
            created_at=datetime.datetime(2008, 1, 1)
        )


@pytest.fixture()
def prepare_entity_setup():
    from ib_discussions.tests.factories.models import EntityFactory
    entity_ids = [
        UUID('31be920b-7b4c-49e7-8adb-41a0c18da848'),
        UUID('4c28801f-7084-4b93-a938-f261aedf8f29'),
        UUID('64eade81-86d0-43d4-9575-d3482aaa30e5'),
        UUID('9cbbe720-9244-441e-b910-1c695b3a7cd1'),
        UUID('da145a02-e164-4203-9317-1d42bb68e3ce'),
        UUID('5c27801f-9084-7b93-a038-f261aedf8f29')
    ]
    for entity_id in entity_ids:
        EntityFactory(id=entity_id)
    return entity_ids