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
    try:
        target_columns = [col for col in ["color_index", "apparent_magnitude", "temperature"] if col in universal_data.columns]
        dt = universal_data.dropna(subset=target_columns).drop_duplicates()
        for col in ["color_index", "ci"]:
            if col in dt.columns:
                dt = dt[dt[col] > 0]
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