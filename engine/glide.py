from typing import Dict, List
from engine.types import AbstractAction

# Composing glides

class StoryMap:
    def __init__(self, glides: Dict[str, List[AbstractAction]]):
        self.glides = glides.copy()

    def __getitem__(self, glide_name):
        return self.glides[glide_name]