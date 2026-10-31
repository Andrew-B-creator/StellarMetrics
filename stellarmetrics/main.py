import pandas as pd
import matplotlib.pyplot as plt
from data_interpreter import process_data
from physics import stellar_physics_processor
from hr_graph_generator import generate_hr_graph



def main():
    file_path, catalog_type, compression = user_input()
    cleaned_data = process_data(file_path,catalog_type, compression = compression)
    processed_data = stellar_physics_processor(cleaned_data)
    generate_hr_graph(processed_data, catalog_type)
    print(f"{catalog_type} Hertzsprung-Russell diagram generated!")




def user_input():
    """Prompt the user for input on what telescope data they want to explore. Currently listed with the samples provided in the code. If data from other telescopes is used, they can be added to the list."""

    catalog_map = {
            "1": ("data/KEPLER_sample.csv", "KEPLER", None),
            "one": ("data/KEPLER_sample.csv", "KEPLER", None),
            "2": ("data/GAIA_sample.csv", "GAIA", None),
            "two": ("data/GAIA_sample.csv", "GAIA", None),
            "3": ("data/HYG_sample.csv", "HYG", None),
            "three": ("data/HYG_sample.csv", "HYG", None),
        }
    print("Welcome to Stellar Metrics! I'm very excited to help you explore stellar data. Please select the telescope data you want to explore today from the list below:")
    print("1: Kepler data")
    print("2: Gaia data")
    print("3: HYG data")
    while True:
        try:
            user_choice = input("Please enter the number corresponding to the telescope you want to explore: ").strip()

            if user_choice not in catalog_map:
                raise Exception("Invalid selection: please choose one of the listed options or type the corresponding number word.")

            file_path, catalog_type, compression = catalog_map[user_choice]

            print(f"You've selected: {catalog_type}.")
            return file_path, catalog_type, compression
        except Exception as e:
            print(f"Error. {e}\n")






if __name__ == "__main__":
    main()