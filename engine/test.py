from engine.glide import StoryMap
from engine.core import NarrativeMachine
from engine.basic import BaseSession

from engine.var import Var, Let, Conditional

from engine.types import AbstractAction, AbstractSession, Performance

class Print(AbstractAction):
    def __init__(self, vartext):
        self.vartext = vartext
    
    def perform(self, session: AbstractSession) -> Performance:
        def view(var):
            return eval(f'f"{self.vartext}"')
        print(view(session.var))
        return Performance.MOVE_ON()

class Input(AbstractAction):
    def __init__(self, prompt, var, parse=None):
        self.var = var
        self.prompt = prompt
        self.parse = parse

    def perform(self, session: AbstractSession) -> Performance:
        answer = input(self.prompt)
        value = self.parse(answer) if self.parse else answer
        session.var._set(self.var, value)
        return Performance.MOVE_ON()

# story logic

story = StoryMap(
    entry = [
        Print("Welcome to this new game"),
        Input("Enter your age: ", Var.age, parse=int),
        Print(f"Ok, your age is: {Var.age}"),
        Conditional(
            smol = lambda var: var.age < 18,
            adult = lambda var: var.age >= 18
        )
    ],

    smol = [
        Print("You're smol !!")
    ],

    adult = [
        Print("You are BIG !!!!!")
    ]
)

# session and narrative machine

from time import sleep

session = BaseSession()

machine = NarrativeMachine(
    session=session,
    glide_map=story,
    prefix_callback=lambda s, a: sleep(0.5),
    error_callback=lambda e, s, p, a: print(e, s, p, a),
    end_callback=lambda s: print('End!'))

if __name__ == '__main__':
    machine.run()