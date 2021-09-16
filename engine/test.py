from engine.types import Performance, AbstractAction, AbstractSession

class Raise(AbstractAction):

    def __init__(self, message):
        self.message = message

    def perform(self, session: AbstractSession) -> Performance:
        raise Exception(self.message)
