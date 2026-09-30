from data_interpreter import clean_data
import pytest 
import pandas as pd
import numpy as np

def test_clean_data():
    dataframe_valid = pd.DataFrame({"ci": [1.0, 2.0, 3.0]})
    assert len(clean_data(dataframe_valid)) == 3

    dataframe_bounds = pd.DataFrame({"ci": [0.0, -1.0, 2.0]})
    res_bounds = clean_data(dataframe_bounds)
    assert len(res_bounds) == 1
    assert res_bounds["ci"].tolist() == [2.0]

    dataframe_nan = pd.DataFrame({"ci": [np.nan, 1.0, 2.0]})
    assert len(clean_data(dataframe_nan)) == 2

    dataframe_all_nan = pd.DataFrame({"ci": [np.nan, np.nan, np.nan]})
    assert len(clean_data(dataframe_all_nan)) == 0
