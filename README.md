# Sensor Plot Generator

This project generates synthetic temperature sensor data and produces scatter, histogram, and box plot visualizations saved as PNG files.

## Installation

1. Activate the `ece105` conda environment:

```bash
conda activate ece105
```

2. Install the required packages:

```bash
conda install numpy matplotlib
```

If you prefer `mamba`, you can also use:

```bash
mamba install numpy matplotlib
```

## Usage

Run the script from the project directory:

```bash
python generate_plots.py
```

## Example output

Running the script produces a single PNG file named `sensor_analysis.png`.

The figure contains three side-by-side plots:

- A scatter plot of sensor temperature readings over time for Sensor A and Sensor B.
- An overlaid histogram showing the temperature distributions for both sensors, with mean lines for each sensor.
- A side-by-side box plot comparing the two sensor distributions, including a horizontal line at the overall mean.

## AI tools used and disclosure

This README content was drafted with the assistance of an AI tool. Any additional disclosure details you need for your project or course requirements go here.