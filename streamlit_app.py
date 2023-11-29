import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
"""
# Analysis steps

Let's try!

"""
# Bouton
if st.button("Appuyez-moi !"):
    st.success(f"Vous avez appuyé sur le bouton. Vous avez saisi : {'Good job!'}")

# Sélecteur de date
selected_date = st.date_input("Sélectionnez une date")

# Sélecteur de temps
selected_time = st.time_input("Sélectionnez l'heure")


