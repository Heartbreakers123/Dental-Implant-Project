import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go
from io import BytesIO

from drug_implant_sim import (
    basic_drug_release,
    surface_degradation,
    burst_release,
    cumulative_release
)

st.set_page_config(page_title="💊 Drug Implant Simulator", layout="wide")
st.title("💊 Drug-Releasing Dental Implant Simulator")
st.markdown("Customize simulation settings below and explore 2D/3D graphs. Optionally download results too.")

st.markdown("---")
col1, col2 = st.columns([2, 1])
simulation_type = col1.selectbox("🧪 Choose Simulation Type", (
    "Basic Drug Release", "Surface Degradation", "Burst Release", "Cumulative Release"
))

use_3d = col2.checkbox("📈 Show 3D Plot (for visual effect)")

st.markdown("### 🔧 Adjust Parameters")

# Param sliders and simulation
if simulation_type == "Basic Drug Release":
    D = st.slider("Diffusion Coefficient (D)", 0.1, 5.0, 1.0)
    r = st.slider("Release Rate (r)", 0.1, 2.0, 0.5)
    t = st.slider("Simulation Time (days)", 1, 30, 10)
    time, release = basic_drug_release(D, r, t)
    ylabel = "Drug Release Amount"

elif simulation_type == "Surface Degradation":
    k = st.slider("Degradation Rate (k)", 0.01, 1.0, 0.1)
    t = st.slider("Simulation Time (days)", 1, 30, 10)
    time, release = surface_degradation(k, t)
    ylabel = "Remaining Material Fraction"

elif simulation_type == "Burst Release":
    D = st.slider("Diffusion Coefficient (D)", 0.1, 5.0, 1.0)
    r = st.slider("Release Rate (r)", 0.1, 2.0, 0.5)
    burst = st.slider("Burst Level", 0.1, 2.0, 0.5)
    t = st.slider("Simulation Time (days)", 1, 30, 10)
    time, release = burst_release(D, r, burst, t)
    ylabel = "Drug Release Amount"

elif simulation_type == "Cumulative Release":
    D = st.slider("Diffusion Coefficient (D)", 0.1, 5.0, 1.0)
    r = st.slider("Release Rate (r)", 0.1, 2.0, 0.5)
    t = st.slider("Simulation Time (days)", 1, 30, 10)
    time, release = cumulative_release(D, r, t)
    ylabel = "Cumulative Drug Released"

# Convert to DataFrame for plotting/export
df = pd.DataFrame({"Time (days)": time, ylabel: release})

# Plotting
st.markdown("### 📊 Visualization")

if use_3d:
    fig = go.Figure(data=[go.Scatter3d(
        x=time,
        y=release,
        z=[0.5]*len(time),
        mode='lines+markers',
        marker=dict(size=5, color=release, colorscale='Viridis'),
        line=dict(width=3)
    )])
    fig.update_layout(
        scene=dict(
            xaxis_title="Time (days)",
            yaxis_title=ylabel,
            zaxis_title="Simulation Z-depth",
            bgcolor="white"  # Set scene background to white
        ),
        paper_bgcolor="white",   # White background outside the 3D plot
        plot_bgcolor="white",    # White background inside plot
        font=dict(color="black"),  # Black text
        title=f"3D Plot - {simulation_type}",
        height=600
    )

    st.plotly_chart(fig, use_container_width=True)
else:
    fig, ax = plt.subplots()
    ax.plot(time, release, color='blue', linewidth=2)
    ax.set_xlabel("Time (days)")
    ax.set_ylabel(ylabel)
    ax.set_title(f"{simulation_type} Profile")
    ax.grid(True)
    st.pyplot(fig)

# Download CSV
st.markdown("### 💾 Download Simulation Data")
buffer = BytesIO()
df.to_csv(buffer, index=False)
buffer.seek(0)
st.download_button(
    label="📥 Download as CSV",
    data=buffer,
    file_name=f"{simulation_type.lower().replace(' ', '_')}.csv",
    mime="text/csv"
)

st.markdown("---")
st.caption("Created By The One And Only HarsH")


