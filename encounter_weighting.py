import random

def get_weighted_encounter_type():
    encounter_type_weights = {
        "Predator": 0.5,
        "Monsters": 5,
        "Enemy NPCs": 1,
        "Neutral NPCs": 1,
        "Friendly NPCs": 1,
        "Faction Event": 1,
        "Points of Interest": 1,
        "Landmarks": 1,
        "No encounter but a fun world detail": 1,
        "Creature": 1,
        "Supernatural encounter": 0.5,
        "Unique Encounter": 0.5,
        "Clue": 1,
        "Obstacle": 2
    }
    encounter_type_names = list(encounter_type_weights.keys())
    encounter_type_probs = [encounter_type_weights[name] for name in encounter_type_names]
    total_weight = sum(encounter_type_probs)
    encounter_type_probs = [weight / total_weight for weight in encounter_type_probs]

    # Choose a random encounter type based on weights
    encounter_type_name = random.choices(encounter_type_names, weights=encounter_type_probs, k=1)[0]
    return encounter_type_name