from ib_boards.interactors.storage_interfaces.dtos import BoardDTO

import factory


class BoardDTOFactory(factory.Factory):
    class Meta:
        model = BoardDTO

    board_id = factory.Sequence(lambda n: f'BOARD_ID_{n + 1}')
    display_name = factory.Sequence(lambda n: f'BOARD_DISPLAY_NAME')
