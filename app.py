# app.py
# Generative Abstract Poster
# Concepts: randomness, lists, loops, functions, matplotlib

import random
import math
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title="Generative Abstract Poster", layout="centered")

st.title("🎨 Generative Abstract Poster")
st.caption("Week 2 • Arts & Advanced Big Data")

# --- Functions ---
def random_palette(k=5):
    # return k random pastel-like colors
    return [(random.random(), random.random(), random.random()) for _ in range(k)]

def blob(center=(0.5, 0.5), r=0.3, points=200, wobble=0.15):
    # generate a wobbly closed shape
    angles = np.linspace(0, 2 * math.pi, points)
    radii = r * (1 + wobble * (np.random.rand(points) - 0.5))
    x = center[0] + radii * np.cos(angles)
    y = center[1] + radii * np.sin(angles)
    return x, y

# --- Sidebar Controls ---
st.sidebar.header("🎛️ Controls")
n_layers = st.sidebar.slider("Number of Layers", 3, 20, 8)
wobble_strength = st.sidebar.slider("Shape Wobble", 0.05, 0.4, 0.15)
random_seed = st.sidebar.number_input("Random Seed (for reproducibility)", value=0, step=1)
generate = st.sidebar.button("🎲 Regenerate Poster")

if generate or random_seed >= 0:
    random.seed(random_seed)

    plt.figure(figsize=(7, 10))
    plt.axis('off')
    plt.gca().set_facecolor((0.98, 0.98, 0.97))

    palette = random_palette(6)
    for i in range(n_layers):
        cx, cy = random.random(), random.random()
        rr = random.uniform(0.15, 0.45)
        x, y = blob(center=(cx, cy), r=rr, wobble=random.uniform(0.05, wobble_strength))
        color = random.choice(palette)
        alpha = random.uniform(0.25, 0.6)
        plt.fill(x, y, color=color, alpha=alpha, edgecolor=(0, 0, 0, 0))

    # simple typographic label
    plt.text(0.05, 0.95, "Generative Poster", fontsize=18, weight='bold', transform=plt.gca().transAxes)
    plt.text(0.05, 0.91, "Week 2 • Arts & Advanced Big Data", fontsize=11, transform=plt.gca().transAxes)

    plt.xlim(0, 1)
    plt.ylim(0, 1)
    st.pyplot(plt)
