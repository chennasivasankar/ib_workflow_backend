from ib_tasks.tests.factories.models import (
    GoFFactory, TaskTemplateWithTransitionFactory, FieldFactory, GoFRoleFactory
)
from ib_tasks.tests.factories.storage_dtos import (
    GoFDTOFactory, GoFRolesDTOFactory, CompleteGoFDetailsDTOFactory,
    GoFRoleDTOFactory, GoFRoleWithIdDTOFactory
)


def reset_sequence(func):
    """
    :param func:
    :return: returns func result
    can be used as decorator to reset the factory sequence to 1
    for the factories listed down here
    """

    def wrapper(*args, **kwargs):
        GoFFactory.reset_sequence(1)
        TaskTemplateWithTransitionFactory.reset_sequence(1)
        FieldFactory.reset_sequence(1)
        GoFRoleFactory.reset_sequence(1)
        GoFDTOFactory.reset_sequence(1)
        GoFRolesDTOFactory.reset_sequence(1)
        CompleteGoFDetailsDTOFactory.reset_sequence(1)
        GoFRoleDTOFactory.reset_sequence(1)
        GoFRoleWithIdDTOFactory.reset_sequence(1)
        result = func(*args, **kwargs)
        return result

    return wrapper
