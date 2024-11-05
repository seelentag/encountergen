from encounter_table import EncounterTable

class EncounterType:
    def __init__(self, name):
        self.name = name
        self.subtables = {}

    def add_subtable(self, subtable_name, entries):
        self.subtables[subtable_name] = EncounterTable(subtable_name, entries)

    def get_subtable(self, subtable_name):
        return self.subtables.get(subtable_name, None)