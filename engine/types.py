from adt import adt, Case
from typing import Callable, Dict, List

class AbstractSession:
    pass


@adt
class Performance:
    MOVE_ON: Case
    BIND: Case[Callable[[AbstractSession, Callable], None], Callable[[AbstractSession], None]]
    JUMP: Case[str]
    JUMP_SUB: Case[str]


class AbstractAction:
    def perform(self, session: AbstractSession) -> Performance:
        raise NotImplementedError

    def is_actual(self, session: AbstractSession) -> bool:
        return True
    
    @property
    def subglides(self) -> Dict[str, List['AbstractAction']]:
        return dict()