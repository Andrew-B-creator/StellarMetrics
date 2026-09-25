import pandas as pd

def retrieve_data():
    url = "https://codeberg.org/astronexus/hyg/media/branch/main/data/hyg/CURRENT/hyg_v44.csv.gz"
    try:
        data = pd.read_csv(url, compression='gzip')
        data.to_csv("stellarmetrics.csv", index = False)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None