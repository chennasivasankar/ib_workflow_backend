from typing import List


class BoardsService:

    @property
    def interface(self):
        # from ib_iam.interfaces.service_interface import ServiceInterface
        # return ServiceInterface()
        pass

    def get_display_boards_and_column_details(self, user_id: str,
                                              board_id: str,
                                              stage_ids: List[str]):
        pass

    def validate_board_id(self, board_id: str):
        pass

