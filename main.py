import random
import streamlit as st
import json
import os
from encounter import Encounter
from encounter_type import EncounterType
from encounter_table import EncounterTable
from flags import EncounterFlags

# Streamlit App Navigation
page = st.sidebar.radio("Select Page", ["Random Encounter Generator", "World Simulation"])

if page == "Random Encounter Generator":
    # Streamlit App - Random Encounter Generator
    st.title("Random Encounter Generator")

    # Select multiple JSON files for generic content
    st.sidebar.header("Select Generic Data Files")
    generic_dir = "generic"
    generic_files = [f for f in os.listdir(generic_dir) if f.endswith('.json')]
    selected_generic_files = st.sidebar.multiselect("Select Generic Data Files", generic_files, default=generic_files)

    # Load all selected generic content files and merge them
    generic_content = {}
    for selected_file in selected_generic_files:
        file_path = os.path.join(generic_dir, selected_file)
        with open(file_path, "r") as generic_file:
            file_content = json.load(generic_file)
            generic_content = {**generic_content, **file_content}

    # Select JSON file for region-specific encounter content
    st.sidebar.header("Select Region")
    regions_dir = "regions"
    region_files = [f for f in os.listdir(regions_dir) if f.endswith('.json')]
    selected_region = st.sidebar.selectbox("Select Region", region_files)
    selected_region_path = os.path.join(regions_dir, selected_region)

    # Load region-specific content
    with open(selected_region_path, "r") as region_file:
        region_content = json.load(region_file)

    # Merge generic and region-specific content
    content = {**generic_content, **region_content}

    # Instantiate Encounter object with content
    encounter_flags = EncounterFlags(content['flags'])
    encounter_generator = Encounter(content)

    # Sidebar for setting encounter flags
    st.sidebar.header("Set Encounter Flags")
    is_stationary = st.sidebar.checkbox("Stationary", False)
    is_traveling = st.sidebar.checkbox("Traveling", True)
    is_night = st.sidebar.checkbox("Night", False)
    is_day = st.sidebar.checkbox("Day", True)
    has_structure = st.sidebar.checkbox("Has Structure", random.choice([True, False]))
    has_water = st.sidebar.checkbox("Has Water", random.choice([True, False]))
    has_road = st.sidebar.checkbox("Has Road", False)

    # Set flags in EncounterFlags object
    encounter_flags.set_flag("is_stationary", is_stationary)
    encounter_flags.set_flag("is_traveling", is_traveling)
    encounter_flags.set_flag("is_night", is_night)
    encounter_flags.set_flag("is_day", is_day)
    encounter_flags.set_flag("has_structure", has_structure)
    encounter_flags.set_flag("has_water", has_water)
    encounter_flags.set_flag("has_road", has_road)

    # Update Encounter object flags
    encounter_generator.flags = encounter_flags.to_dict()

    # Generate encounter button
    if st.button("Generate Encounter"):
        encounter = encounter_generator.generate_encounter()
        st.subheader("Generated Encounter")
        for key, value in encounter.items():
            st.text(f"{key}: {value}")
