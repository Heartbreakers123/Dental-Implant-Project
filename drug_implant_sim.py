import numpy as np
import matplotlib.pyplot as plt

# ---------- Basic Drug Release Simulation ----------
def basic_drug_release(D=1.0, r=0.5, t=10):
    time = np.linspace(0, t, 100)
    release = D * (1 - np.exp(-r * time))
    return time, release

# ---------- Surface Degradation Simulation ----------
def surface_degradation(k=0.1, t=10):
    time = np.linspace(0, t, 100)
    degradation = np.exp(-k * time)
    return time, degradation

# ---------- Burst Release Simulation ----------
def burst_release(D=1.0, r=0.5, burst_level=0.5, t=10):
    time = np.linspace(0, t, 100)
    release = D * (1 - np.exp(-r * time)) + burst_level
    return time, release

# ---------- Cumulative Release Profile ----------
def cumulative_release(D=1.0, r=0.5, t=10):
    time = np.linspace(0, t, 100)
    release_rate = D * r * np.exp(-r * time)
    cumulative = np.cumsum(release_rate) * (t / len(time))
    return time, cumulative

