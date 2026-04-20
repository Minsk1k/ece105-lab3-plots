"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""

# Create a function generate_data(seed) that returns sensor_a, sensor_b,
# and timestamps arrays with the same parameters as in the notebook.
# Use NumPy-style docstring with Parameters and Returns sections.

import numpy as np  # generating synthetic data
import matplotlib.pyplot as plt  # for creating visualizations
np.random.seed(19)

def generate_data(seed, n_readings=200, duration=10.0):
    """
    Generate synthetic temperature sensor data for two sensors.

    Parameters
    ----------
    seed : int
        Seed to initialize NumPy's random number generator for reproducible output.
    n_readings : int, optional
        Number of sensor readings to generate. Default is 200.
    duration : float, optional
        Maximum timestamp value in seconds. Default is 10.0.

    Returns
    -------
    timestamps : ndarray of shape (n_readings,)
        Sorted timestamps from 0 to `duration` seconds.
    sensor_a : ndarray of shape (n_readings,)
        Temperature readings for Sensor A sampled from a normal distribution
        with mean 25°C and standard deviation 3°C.
    sensor_b : ndarray of shape (n_readings,)
        Temperature readings for Sensor B sampled from a normal distribution
        with mean 27°C and standard deviation 4.5°C.
    """
    rng = np.random.default_rng(seed)

    timestamps = rng.uniform(0.0, duration, n_readings)
    sensor_a = rng.normal(loc=25.0, scale=3.0, size=n_readings)
    sensor_b = rng.normal(loc=27.0, scale=4.5, size=n_readings)

    sort_idx = np.argsort(timestamps)

    return (
        timestamps[sort_idx],
        sensor_a[sort_idx],
        sensor_b[sort_idx],
    )

# Create plot_scatter(sensor_a, sensor_b, timestamps, ax) that draws
# the scatter plot from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.

def plot_scatter(sensor_a, sensor_b, timestamps, ax):
    """
    Plot scatter plot of sensor data on the given Axes object.

    This function creates a scatter plot showing temperature readings
    from two sensors over time, with Sensor A in blue and Sensor B in orange.

    Parameters
    ----------
    sensor_a : array_like
        Temperature readings for Sensor A, shape (200,).
    sensor_b : array_like
        Temperature readings for Sensor B, shape (200,).
    timestamps : array_like
        Timestamps corresponding to readings, shape (200,).
    ax : matplotlib.axes.Axes
        The Axes object on which to draw the plot.

    Returns
    -------
    None
        Modifies the input Axes object in place.
    """
    ax.scatter(timestamps, sensor_a, color='blue', label='Sensor A', alpha=0.7)
    ax.scatter(timestamps, sensor_b, color='orange', label='Sensor B', alpha=0.7)
    ax.set_xlabel('Time (seconds)')
    ax.set_ylabel('Temperature (°C)')
    ax.set_title('Scatter Plot of Sensor Data')
    ax.legend()
    ax.grid(True)