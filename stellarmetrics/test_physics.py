import pytest
import pandas as pd
import physics
import numpy as np

Sol_CI = .656
Sol_APMG = -26.74
Sol_Distance_Parsec = 0.0000048481 
"""These are the values for the Sun's B-V color index, apparent magnitude, and distance in parsecs.
APMG stands for apparent magnitude. CI stands for color index (B-V color index, to be exact)."""


def test_ballesteros_temperature_calculation():
    calculated_temp = physics.ballesteros_temperature_calculation(Sol_CI)
    assert abs(calculated_temp -5757) <10

def test_absolute_magnitude_calculation():
    calculated_abs_mag = physics.absolute_magnitude_calculation(Sol_APMG, Sol_Distance_Parsec)
    assert abs(calculated_abs_mag - 4.83) < 0.1

def test_absolute_magnitude_invalid_distance():
    with pytest.raises(ValueError):
        physics.absolute_magnitude_calculation(apparent_magnitude = 10.0, distance_parsec = -5.0)
    with pytest.raises(ValueError):
        physics.absolute_magnitude_calculation(apparent_magnitude = 10.0, distance_parsec = 0.0)


def test_absolute_magnitude_vectorization():
    apparent_magnitudes = pd.Series([10.0, 5.0, 2.0])
    distances = pd.Series([10.0, 20.0, 5.0])
    calculated_abs_mags = physics.absolute_magnitude_calculation(apparent_magnitudes, distances)
    expected = pd.Series([10.0 - 5 * (np.log10(10.0) - 1.0),
                          5.0 - 5 * (np.log10(20.0) - 1.0),
                          2.0 - 5 * (np.log10(5.0) - 1.0)])
    assert np.allclose(calculated_abs_mags, expected, atol = 1e-3)

def test_luminosity_calculation():
    calculated_luminosity = physics.luminosity_calculation(4.83)
    assert abs(calculated_luminosity - 1.0) < 0.01

def test_radius_calculation():
    calculated_radius = physics.radius_calculation(luminosity = 1.0, temperature = 5778.0)
    assert abs(calculated_radius - 1.0) < 0.01
    
def test_radius_calculation_invalid_values():
    with pytest.raises(ValueError):
        physics.radius_calculation(luminosity = -1.0, temperature = 5778.0)
    with pytest.raises(ValueError):
        physics.radius_calculation(luminosity = 1.0, temperature = -5778.0)

def test_parallax_to_distance():
    calculated_distance = physics.parallax_to_distance(100.0)
    assert abs(calculated_distance - 10.0) < 0.01

def test_parallax_to_distance_invalid_values():
    with pytest.raises(ValueError):
        physics.parallax_to_distance(-100.0)
    with pytest.raises(ValueError):
        physics.parallax_to_distance(0.0)

def test_error_propagation_calculation():
    calculated_error = physics.error_propagation_calculation(parallax_mas = 100.0, parallax_error_mas = 10.0)
    assert np.isclose(calculated_error, 1.0)

def test_magnitude_error_calculation():
    calculated_magnitude_error = physics.magnitude_error_calculation(apparent_magnitude_noise = 0.1, parallax_noise = 0.01, parallax = 100.0)
    assert np.isclose(calculated_magnitude_error, 0.1)