import pandas as pd
import numpy as np


def ballesteros_temperature_calculation(color_index):
    """Calculates the surface temperature of a star in Kelvin based on B-V color index"""
    Term_1 =  1.0/(.92 * color_index + 1.7)
    Term_2 =  1.0/(.92 * color_index + .62)
    temperature = 4600*(Term_1 + Term_2)
    return temperature

def absolute_magnitude_calculation(apparent_magnitude, distance_parsec = None, parallax_mas = None):
    """Calculates the absolute magnitude of a star given its apparent magnitude and distance/parallex"""
    if distance_parsec is None and parallax_mas is None:
        raise ValueError("A positive distance must be provided for either distance_parsec or parallax_mas")
    
    if distance_parsec is None and parallax_mas is not None:
        effective_distance = 1000.0/parallax_mas
    
    elif parallax_mas is None:
        effective_distance = distance_parsec

    else:
        effective_distance = np.where(distance_parsec > 0, distance_parsec, 1000.0/parallax_mas)

    effective_distance = np.where(effective_distance > 0, effective_distance, np.nan)
    return apparent_magnitude - 5 * (np.log10(effective_distance) - 1.0)
  
def parallax_to_distance(parallax_mas):
    """Converts parallax in milliarcseconds to distance in parsecs"""
    parallax_mas = np.where(parallax_mas > 0, parallax_mas, np.nan)
    return 1000.0 / parallax_mas

def luminosity_calculation(absolute_magnitude):
    """Calculates the luminosity of a star in solar luminosities based on its absolute magnitude"""
    luminosity = 10.0 ** (-0.4*(absolute_magnitude - 4.83))
    return luminosity

def radius_calculation(luminosity, temperature):
    """Calculates the radius of a star in solar radii based on its luminosity and temperature"""
    with np.errstate(invalid='ignore'):
        radius = np.sqrt(luminosity) * (5778.0/temperature)**2
    return radius

def error_propagation_calculation(parallax_mas, parallax_error_mas):
    parallax_value = parallax_mas
    parallax_error = parallax_error_mas
    distance_uncertainty_value = 1000/(parallax_value**2) * parallax_error

    return distance_uncertainty_value

def magnitude_error_calculation(apparent_magnitude_noise, parallax_noise, parallax):
    magnitude_error = np.sqrt(apparent_magnitude_noise**2 + ((5/np.log(10)*parallax_noise/parallax)**2))
    return magnitude_error


def stellar_physics_processor(df):
    """Processes a dataframe containing stellar data and calculates derived physical properties using the above functions"""
    df = df.copy()
    if "temperature" not in df.columns:
        if "teff" in df.columns:
            df["temperature"] = df["teff"]
        elif "color_index" in df.columns:
            df["temperature"] = ballesteros_temperature_calculation(df["color_index"])
    
    if "parallax_mas" not in df.columns and "distance_parsec" in df.columns:
        df["parallax_mas"] = 1000.0 / df["distance_parsec"]

    if "apparent_magnitude" in df.columns and ("parallax_mas" in df.columns or "distance_parsec" in df.columns):
        df["absolute_magnitude"] = absolute_magnitude_calculation(df.get("apparent_magnitude"), distance_parsec = df.get("distance_parsec"), parallax_mas = df.get("parallax_mas"))
        df["luminosity"] = luminosity_calculation(df["absolute_magnitude"])
        if "radius" not in df.columns and "temperature" in df.columns:
            df["radius"] = radius_calculation(df["luminosity"], df["temperature"])
    if "luminosity" not in df.columns and "radius" in df.columns and "temperature" in df.columns:
        df["luminosity"] = (df["radius"]**2) * ((df["temperature"]/5778.0)**4)
    
    if "parallax_mas" in df.columns and "parallax_error_mas" in df.columns:
        df["distance_uncertainty"] = error_propagation_calculation(df["parallax_mas"], df["parallax_error_mas"])
    
    if "apparent_magnitude_noise" in df.columns and "parallax_noise" in df.columns and "parallax_mas" in df.columns:
        df["magnitude_error"] = magnitude_error_calculation(df["apparent_magnitude_noise"], df["parallax_noise"], df["parallax_mas"])
    return df
