from ib_tasks.interactors.stages_dtos import StageLogicAttributes


class StageDisplayLogicInteractor:
    def __init__(self):
        pass

    @staticmethod
    def get_stage_display_logic_attributes(stage_display_logic: str):
        return StageLogicAttributes(
            stage_id="PR_PENDING RP APPROVAL",
            status_id="status10"
        )
