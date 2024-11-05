import random

def get_behavior_and_awareness_for_type(encounter_type_name, behaviors):
    behavior = "N/A"
    awareness_entry = "N/A123"

    # Define behavior tables for each type of encounter
    behavior_table_mapping = {
        "Monsters": "Generic Monster Behavior",
        "Enemy NPCs": "Enemy NPC Behavior",
        "Neutral NPCs": "Neutral NPC Behavior",
        "Friendly NPCs": "Friendly NPC Behavior"
    }
    
    # Get behavior based on encounter type
    if encounter_type_name in behavior_table_mapping:
        behavior_table_key = behavior_table_mapping[encounter_type_name]
        behavior_table = behaviors.get_subtable(behavior_table_key)

        # Assuming `get_subtable()` returns an `EncounterTable` object, which might not be iterable
        if behavior_table and hasattr(behavior_table, 'get_entries'):
            # Convert the entries into a list to use with `random.choice()`
            behavior_entries = behavior_table.get_entries()  # Assuming this returns a list of entries
            behavior = random.choice(behavior_entries) if behavior_entries else "No specific behavior"
        else:
            behavior = "No specific behavior"

    # Get awareness based on encounter type
    awareness_levels = ["Unaware", "Slightly Aware", "Partially Aware", "Fully Aware"]
    awareness_level = random.choice(awareness_levels)

    # Depending on the encounter type, access the correct awareness subtable
    if encounter_type_name in ["Monsters", "Enemy NPCs"]:
        npc_awareness = behaviors.get_subtable("NPC Awareness")
        hostile_awareness = npc_awareness.get_subtable("Hostile") if npc_awareness else None
        if hostile_awareness and hasattr(hostile_awareness, 'get_subtable'):
            awareness_table = hostile_awareness.get_subtable(awareness_level)
            awareness_list = awareness_table.get_entries() if awareness_table else ["No specific awareness entry"]
        else:
            awareness_list = ["No specific awareness entry"]

    elif encounter_type_name == "Neutral NPCs":
        npc_awareness = behaviors.get_subtable("NPC Awareness")
        neutral_awareness = npc_awareness.get_subtable("Neutral") if npc_awareness else None
        if neutral_awareness and hasattr(neutral_awareness, 'get_subtable'):
            awareness_table = neutral_awareness.get_subtable(awareness_level)
            awareness_list = awareness_table.get_entries() if awareness_table else ["No specific awareness entry"]
        else:
            awareness_list = ["No specific awareness entry"]

    elif encounter_type_name == "Friendly NPCs":
        npc_awareness = behaviors.get_subtable("NPC Awareness")
        friendly_awareness = npc_awareness.get_subtable("Friendly") if npc_awareness else None
        if friendly_awareness and hasattr(friendly_awareness, 'get_subtable'):
            awareness_table = friendly_awareness.get_subtable(awareness_level)
            awareness_list = awareness_table.get_entries() if awareness_table else ["No specific awareness entry"]
        else:
            awareness_list = ["No specific awareness entry"]

    else:
        awareness_list = ["No specific awareness entry"]

    awareness_entry = random.choice(awareness_list)

    return behavior, awareness_entry