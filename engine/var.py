from typing import Callable, Any, Dict, List
from engine.types import Performance, AbstractAction, AbstractSession

from dataclasses import dataclass
from adt import adt, Case

# Variable objects

class VarStore:
    def __init__(self):
        self.__dict__['_data'] = dict()

    def __getattr__(self, name):
        if name in self._data.keys():
            return self._data[name]
        else:
            raise NameError

    def __setattr__(self, name, value):
        if not name.startswith('_'):
            self._data[name]
        else:
            raise AttributeError
    
    def _export(self):
        pass

    def _access(self, varkey):
        return self._data[varkey.name]

    def _set(self, varkey, value):
        self._data[varkey.name] = value


@dataclass
class VarKey:
    name: str

    def __format__(self, format_spec):
        return "{var.$}".replace('$', self.name)


class VarManager:
    def __getattribute__(self, name):
        return VarKey(name)

    # special decorator for converting normal functions to Var-eating capable
    # todo


Var = VarManager()


class VarSession(AbstractSession):
    var: VarStore


# Actions for variable manipulation

class Eval(AbstractAction):
    def __init__(self, func: Callable[[VarStore], None]):
        self.func = func

    def perform(self, session) -> Performance:
        self.func(session.var)
        return Performance.MOVE_ON()


class Let(AbstractAction):
    def __init__(self, **varops: Callable[[VarStore], Any]):
        self.varops = varops

    def perform(self, session : VarSession) -> Performance:
        for varname, varop in self.varops.items():
            session.var._data[varname] = varop(session.var)
        return Performance.MOVE_ON()


# Moving around glides

@adt 
class MatchMode:
    WEAK: Case
    STRICT: Case
    FALLBACK: Case[str]

# lil helper
def _raise(ex):
    def cb():
        raise ex
    return cb

class Jump(AbstractAction):
    def __init__(self, value_key: VarKey, jump_map: Dict[Any, str], mode=MatchMode.WEAK()):
        self.value_key = value_key
        self.jump_map = jump_map
        self.mode = mode

    def perform(self, session : VarSession) -> Performance:
        value = session.var._access(self.value_key)
        if value not in self.jump_map.keys():
            return self.mode.match(
                weak=Performance.MOVE_ON,
                strict=_raise(KeyError),
                fallback=Performance.JUMP
            )
        else:
            return Performance.JUMP(self.jump_map[value])

@dataclass
class Proceed(AbstractAction):

    glide_name: str

    def perform(self, session : VarSession) -> Performance:
        return Performance.JUMP(self.glide_name)


class Switch(AbstractAction):
    def __init__(self, value_key: VarKey, local_glides: Dict[str, List[AbstractAction]], mode=MatchMode.WEAK()):
        self.value_key = value_key
        self.glides = local_glides
        self.mode = mode
    
    @property
    def subglides(self):
        return self.glides

    def perform(self, session : VarSession) -> Performance:
        glide_name = session.var._access(self.value_key)
        if glide_name not in self.glides.keys():
            return self.mode.match(
                weak=Performance.MOVE_ON,
                strict=_raise(KeyError),
                fallback=Performance.JUMP_SUB
            )
        else:
            return Performance.JUMP_SUB(glide_name)


class Conditional(AbstractAction):
    def __init__(self, mode=MatchMode.WEAK(), **conditions: Callable[[VarStore], bool]):
        self.mode = mode
        self.conditions = conditions

    def perform(self, session : VarSession) -> Performance:
        for glide_name, condition in self.conditions.items():
            if condition(session.var): return Performance.JUMP(glide_name)
        else:
            return self.mode.match(
                weak=Performance.MOVE_ON,
                strict=_raise(KeyError),
                fallback=Performance.JUMP
            )
