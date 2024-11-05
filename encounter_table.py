
import random

class EncounterTable:
    def __init__(self, name, entries):
        self.name = name
        self.entries = entries

    def get_random_entry(self):
        return random.choice(self.entries)