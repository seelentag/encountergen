class EncounterFlags:
    def __init__(self, flags_dict):
        self.flags = flags_dict

    def is_structure(self):
        return self.flags.get("has_structure", False)

    def is_water(self):
        return self.flags.get("has_water", False)

    def is_road(self):
        return self.flags.get("has_road", False)

    def is_day(self):
        return self.flags.get("is_day", False)

    def is_night(self):
        return self.flags.get("is_night", False)

    def set_flag(self, key, value):
        self.flags[key] = value

    def to_dict(self):
        return self.flags
