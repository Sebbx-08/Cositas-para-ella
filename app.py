import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def draw_cinnamoroll_and_flowers():
    fig, ax = plt.subplots(figsize=(8,8))
    ax.axis('off')
    # Aquí adapta tu dibujo de Cinnamoroll y flores usando Matplotlib
    # Por ejemplo, dibuja círculos y formas que simulan el dibujo original
    circle = plt.Circle((0.5, 0.5), 0.4, color='white', ec='black', lw=3)
    ax.add_artist(circle)
    ax.text(0.5, 0.1, "Tal vez es un poco pronto pero no queria que pasaras el dia sin tus flores amarillas, te quiero mi niña <3", 
            fontsize=12, color='black', fontweight='bold', ha='center', wrap=True)
    return fig

st.title("Flores amarillas para mi niña <3")
fig = draw_cinnamoroll_and_flowers()
st.pyplot(fig)