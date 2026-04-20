"""Generate publication-quality sensor data visualizations.
 
This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.
 
Usage
-----
    python generate_plots.py
"""
 
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
 
 
def plot_scatter(sensor_a, sensor_b, timestamps, ax):
    """
    Plot scatter plot of sensor data on the given Axes object.
 
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
 
 
def plot_histogram(sensor_a, sensor_b, ax):
    """
    Plot overlaid histogram of sensor temperature distributions on the given Axes object.
 
    Parameters
    ----------
    sensor_a : array_like
        Temperature readings for Sensor A, shape (200,).
    sensor_b : array_like
        Temperature readings for Sensor B, shape (200,).
    ax : matplotlib.axes.Axes
        The Axes object on which to draw the plot.
 
    Returns
    -------
    None
        Modifies the input Axes object in place.
    """
    ax.hist(sensor_a, bins=30, alpha=0.5, label='Sensor A', color='blue')
    ax.hist(sensor_b, bins=30, alpha=0.5, label='Sensor B', color='orange')
    ax.axvline(np.mean(sensor_a), color='blue', linestyle='--', linewidth=2, label='Sensor A Mean')
    ax.axvline(np.mean(sensor_b), color='orange', linestyle='--', linewidth=2, label='Sensor B Mean')
    ax.set_xlabel('Temperature (°C)')
    ax.set_ylabel('Frequency')
    ax.set_title('Overlaid Histogram of Sensor Temperature Distributions')
    ax.legend()
    ax.grid(True, alpha=0.3)
 
 
def plot_boxplot(sensor_a, sensor_b, ax):
    """
    Plot side-by-side box plot of sensor distributions on the given Axes object.
 
    Parameters
    ----------
    sensor_a : array_like
        Temperature readings for Sensor A, shape (200,).
    sensor_b : array_like
        Temperature readings for Sensor B, shape (200,).
    ax : matplotlib.axes.Axes
        The Axes object on which to draw the plot.
 
    Returns
    -------
    None
        Modifies the input Axes object in place.
    """
    ax.boxplot([sensor_a, sensor_b], tick_labels=['Sensor A', 'Sensor B'])
    overall_mean = np.mean(np.concatenate([sensor_a, sensor_b]))
    ax.axhline(overall_mean, color='red', linestyle='--', linewidth=2, label=f'Overall Mean: {overall_mean:.2f}°C')
    ax.set_ylabel('Temperature (deg C)')
    ax.set_title('Side-by-Side Box Plot of Sensor Distributions')
    ax.legend()
    ax.grid(True, axis='y', alpha=0.3)
 
 
def main():
    """
    Generate sensor data and create publication-quality visualizations.
 
    Parameters
    ----------
    None
 
    Returns
    -------
    None
    """
    # Generate synthetic data for both sensors using a fixed seed.
    timestamps, sensor_a, sensor_b = generate_data(1234)
 
    # Create a 2x2 grid of subplots; the fourth cell will be left empty.
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
 
    # Draw each plot on its own Axes object using 2D indexing.
    plot_scatter(sensor_a, sensor_b, timestamps, axes[0, 0])
    plot_histogram(sensor_a, sensor_b, axes[0, 1])
    plot_boxplot(sensor_a, sensor_b, axes[1, 0])
 
    # Hide the unused fourth cell.
    axes[1, 1].set_visible(False)
 
    # Improve spacing between subplots so labels and titles do not overlap.
    plt.tight_layout()
 
    # Save the complete figure to disk as a high-resolution PNG file.
    plt.savefig('sensor_analysis.png', dpi=150, bbox_inches='tight')
    print("Plot saved as sensor_analysis.png")
 
 
if __name__ == '__main__':
    # Run the main workflow only when the script is executed directly.
    main()