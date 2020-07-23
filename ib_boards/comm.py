from ib_boards.interactors.dtos import GetBoardsDTO
from ib_boards.interactors.get_boards_interactor import GetBoardsInteractor
from ib_boards.presenters.presenter_implementation import GetBoardsPresenterImplementation
from ib_boards.storages.storage_implementation import StorageImplementation


boards_dto = GetBoardsDTO(
        user_id=1,
        offset=0,
        limit=4
    )

storage = StorageImplementation()
presenter = GetBoardsPresenterImplementation()

interactor = GetBoardsInteractor(
        storage=storage
    )
response = interactor.get_boards_wrapper(presenter=presenter,
                                             get_boards_dto=boards_dto)

