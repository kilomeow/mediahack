from typing import Dict, List
from engine.types import AbstractAction

# Composing glides

class StoryMap:
    def __init__(self, entry: List[AbstractAction], **glides: List[AbstractAction]):
        self.glides = glides.copy()
        self.glides['entry'] = entry

    def __getitem__(self, glide_name):
        return self.glides[glide_name]