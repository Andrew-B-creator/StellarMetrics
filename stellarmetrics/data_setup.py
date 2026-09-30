import pandas as pd



""" Data_setup.py serves as a utility script to download and sample data from various astronomical databases. 
The sample data is already localized within the 'data' folder within Stellarmetrics. The following code simply demonstrates how the data was downloaded. 
This file isn't needed to make the program run smoothly once the data is sampled and downloaded, it is simply being kept here to showcase the process. 
In addition, if any more datasets are to be added by another user in the future, the sample data downloaded here and uploaded into the data folder as the data below has been."""


hyg_dataframe = pd.read_csv("https://codeberg.org/astronexus/hyg/media/branch/main/data/hyg/CURRENT/hyg_v44.csv.gz", compression='gzip', nrows = 10000)
hyg_dataframe.to_csv("data/HYG_sample.csv", index = False)

gaia_dataframe = pd.read_csv("https://gea.esac.esa.int/tap-server/tap/sync?REQUEST=doQuery&LANG=ADQL&FORMAT=CSV&QUERY=SELECT+TOP+10000+source_id,ra,dec,parallax,parallax_error,phot_g_mean_mag,bp_rp+FROM+gaiadr3.gaia_source+WHERE+parallax%3E1", nrows = 10000)
gaia_dataframe.to_csv("data/GAIA_sample.csv", index = False)

kepler_dataframe = pd.read_csv("https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+kepid,ra,dec,teff,radius+from+keplerstellar&format=csv", nrows=10000)
kepler_dataframe.to_csv("data/KEPLER_sample.csv", index = False)