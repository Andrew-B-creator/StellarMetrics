import pandas as py
import matplotlib.pyplot as plt
from data_interpreter import retrieve_data

print("Hello, welcome to Stellar Metrics! I'm very excited to help you explore stellar data.")

try:
    dt = retrieve_data()
    print("Data has been loaded successfully,")
    print("Data has been saved to 'stellarmetrics.csv'.")

    print(dt[["proper", "ci", "absmag", "lum"]].head())
    
except Exception as e:
    print(f"Error loading data: {e}")
