import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
"""
# Analysis steps

Let's try!

"""
# Bouton
if st.button("Push!"):
    st.success(f"You pushed: {'Good boy!'}")

# Sélecteur de date
start_date = st.date_input("Select a beginning day")
end_date = st.date_input("Select an end day")

# Sélecteur de temps
selected_time = st.time_input("Sélectionnez l'heure")


