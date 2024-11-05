import random
from encounter_table import EncounterTable
from encounter_type import EncounterType
from encounter_weighting import get_weighted_encounter_type
from encounter_details import generate_terrain_detail, generate_visibility
from behavior_awareness import get_behavior_and_awareness_for_type

class Encounter:
    def __init__(self, content):
        # Initialization logic (same as before)
        self.terrain_details = EncounterType("Terrain Details")
        for subtable_name, entries in content['terrain_details'].items():
            self.terrain_details.add_subtable(subtable_name, entries)
        
        self.weather_conditions = EncounterTable("Weather Conditions", content['weather_conditions'])
        
        self.visibility = EncounterType("Visibility and Light")
        for subtable_name, entries in content['visibility'].items():
            self.visibility.add_subtable(subtable_name, entries)
        
        self.navigation_difficulty = EncounterTable("Navigation Difficulty", content['navigation_difficulty'])
        
        # Encounter types with subtables setup
        self.encounter_types = {}
        for encounter_type_name, subtables in content['encounter_types'].items():
            encounter_type = EncounterType(encounter_type_name)
            for subtable_name, entries in subtables.items():
                encounter_type.add_subtable(subtable_name, entries)
            self.encounter_types[encounter_type_name] = encounter_type
        
        # Behavior subtables
        self.behaviors = EncounterType("Behavior")
        for subtable_name, entries in content['behaviors'].items():
            self.behaviors.add_subtable(subtable_name, entries)
        
        # Awareness subtables
        self.awareness = EncounterType("Awareness")
        for subtable_name, entries in content['awareness'].items():
            self.awareness.add_subtable(subtable_name, entries)
        
        self.player_position = EncounterTable("Player Position", content['player_position'])
        
        # Context flags
        self.flags = content['flags']

    def get_specific_type_for_encounter(self, encounter_type_name):
        specific_type = "N/A"
        encounter_type = self.encounter_types.get(encounter_type_name)
        if encounter_type and encounter_type.subtables:
            specific_type_table = encounter_type.get_subtable(random.choice(list(encounter_type.subtables.keys())))
            if specific_type_table:
                specific_type = specific_type_table.get_random_entry()
        return specific_type

    def generate_encounter(self):
        # Use helper function to select encounter type using weighting
        encounter_type_name = get_weighted_encounter_type()

        # Use helper function to generate terrain details
        terrain_detail = generate_terrain_detail(self.flags, self.terrain_details)

        # Use helper function to generate visibility
        visibility = generate_visibility(self.flags, self.visibility)

        # Determine specific type for encounter
        specific_type = self.get_specific_type_for_encounter(encounter_type_name)

        # Determine behavior and awareness based on encounter type
        behavior, awareness = get_behavior_and_awareness_for_type(encounter_type_name, self.behaviors)
        
        # Generate complete encounter details
        encounter_details = {
            "Terrain Details": terrain_detail,
            "Weather Conditions": self.weather_conditions.get_random_entry(),
            "Visibility and Light": visibility,
            "Navigation Difficulty": self.navigation_difficulty.get_random_entry(),
            "Encounter Type": encounter_type_name,
            "Specific Type": specific_type,
            "Player Position": self.player_position.get_random_entry(),
            "Behavior": behavior,
            "Awareness": awareness,
            "Flags": self.flags
        }

        return encounter_details
