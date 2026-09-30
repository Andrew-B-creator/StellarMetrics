import pandas as pd
import numpy as np
import mapper



def retrieve_data(user_choice, compression = None):
    try:
        data = pd.read_csv(user_choice, compression=compression)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None


def clean_data(universal_data):
    if "color_index" not in universal_data.columns:
        print("Error: 'color index' column not found in data.")
        return None
    try:
        dt = universal_data.dropna(subset=["color_index", "apparent_magnitude"]).drop_duplicates()
        return dt

    except Exception as e:
        print(f"Error cleaning data: {e}")
        return None
    
def process_data(user_choice, catalog_type, compression = None):
    data = retrieve_data(user_choice, compression=compression)
    if data is None:
        return None
    universal_data = mapper.unify_map_columns(data, catalog_type)
    cleaned_data = clean_data(universal_data)
    return cleaned_data