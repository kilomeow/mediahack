from engine.var import Var, VarSession, VarStore
from engine.core import HistorySession

from typing import Dict, List

from dataclasses import dataclass, field


@dataclass
class BaseSession(VarSession, HistorySession):
    history: List[str] = field(default_factory=list)
    progress: Dict[str, int] = field(default_factory=dict)
    var: VarStore = field(default_factory=VarStore)
