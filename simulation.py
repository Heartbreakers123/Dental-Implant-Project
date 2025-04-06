import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objs as go

# Simulation 1: Basic Drug Release
def simulate_drug_release(time_days, release_constant):
    return release_constant * np.sqrt(time_days)

# Simulation 2: Coating Degradation
def simulate_degradation(time_days, initial_thickness, degradation_rate):
    return initial_thickness - degradation_rate * time_days

# Simulation 3: Cumulative Drug Release
def simulate_cumulative_release(time_days, initial_dose, decay_rate):
    return initial_dose * (1 - np.exp(-decay_rate * time_days))

# Simulation 4: Interactive parameter slider-based release
def release_with_params(time, release_rate):
    return release_rate * np.log1p(time)

def degradation_with_params(time, degradation_rate):
    return np.maximum(0, 50 - degradation_rate * time)

# Simulation 5: 3D Drug Release Visualization
def get_3d_drug_release_data():
    time = np.linspace(0, 30, 50)
    thickness = np.linspace(10, 40, 50)
    release_rate = 1.2 * np.exp(-0.05 * time) + 0.1 * np.sin(thickness / 5)
    return time, thickness, release_rate

def plot_3d_release(time, thickness, release_rate):
    trace = go.Scatter3d(
        x=time,
        y=thickness,
        z=release_rate,
        mode='markers+lines',
        marker=dict(
            size=6,
            color=release_rate,
            colorscale='Plasma',
            colorbar=dict(title='Release Rate')
        )
    )

    layout = go.Layout(
        title='\U0001F48A 3D Drug Release & Degradation Model',
        scene=dict(
            xaxis_title='Time (days)',
            yaxis_title='Coating Thickness (µm)',
            zaxis_title='Drug Release Rate (mg/cm³/day)'
        ),
        height=600
    )

    fig = go.Figure(data=[trace], layout=layout)
    return fig

