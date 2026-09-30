import pandas as pd
import matplotlib.pyplot as plt
from data_interpreter import process_data
from physics import stellar_physics_processor



def main():
    file_path, catalog_type, compression = user_input()
    cleaned_data = process_data(file_path,catalog_type, compression = compression)
    print("Available noise/error columns:", [col for col in cleaned_data.columns if any(term in col.lower() for term in ['err', 'noise', 'unc', 'e_'])])
    processed_data = stellar_physics_processor(cleaned_data)
    




def user_input():
    """Prompt the user for input on what telescope data they want to explore. Currently listed with the samples provided in the code. If data from other telescopes is used, they can be added to the list."""
    try:
        print("Welcome to Stellar Metrics! I'm very excited to help you explore stellar data. Please select the telescope data you want to explore today from the list below:")
        print("1: Kepler data")
        print("2: Gaia data")
        print("3: HYG data")
        user_choice = input("Please enter the number corresponding to the telescope you want to explore: ").strip()

        catalog_map = {
            "1": ("data/KEPLER_sample.csv", "KEPLER", None),
            "2": ("data/GAIA_sample.csv", "GAIA", None),
            "3": ("data/HYG_sample.csv", "HYG", None),
        }
        if user_choice not in catalog_map:
            raise Exception("Invalid selection; please choose one of the listed options.")
        
        file_path, catalog_map, compression = catalog_map[user_choice]
        

        print(f"You've selected: {catalog_map}. Let's get started!")
        return file_path, catalog_map, compression

    except Exception as e:
        print(f"Error getting user input: {e}. Please enter a valid integer.")
        return None





if __name__ == "__main__":
    main()