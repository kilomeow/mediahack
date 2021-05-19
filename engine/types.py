from adt import adt, Case
from typing import Callable, Dict, List

@adt
class Performance:
    MOVE_ON: Case
    BIND: Case[Callable]
    JUMP: Case[str]
    JUMP_SUB: Case[str]


class AbstractSession:
    pass


class AbstractAction:
    def perform(self, session: AbstractSession) -> Performance:
        raise NotImplementedError

    def is_actual(self, session: AbstractSession) -> bool:
        return True
    
    @property
    def subglides(self) -> Dict[str, List['AbstractAction']]:
        return dict()