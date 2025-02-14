import numpy as np
import streamlit as st

st.title("Ladder Padder")
st.text(
    """Welcome to Ladder Padder\n\n             |‾‾‾‾\n             |\n            /|\n            / |\n            /  |\n            /   |\n            /    |\n        /     |\n        /      |\n        /       |\n        /        |\n    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾"""
)

h_min = st.number_input("Height of lowest windowsill: ")
h_max = st.number_input("Height of highest windowsill: ")
el = st.number_input("Distance below grade: ")

theta_min = np.deg2rad(st.number_input("Minimum ladder angle", value=70.0))
theta_max = np.deg2rad(st.number_input("Maximum ladder angle", value=76.0))

d_min = (h_min + el) / np.tan(theta_max)
d_max = (h_max + el) / np.tan(theta_min)
width = d_max - d_min

st.write("Minimum ladder pad wall distance: ", round(d_min, 1))
st.write("Maximum ladder pad wall distance: ", round(d_max, 1))
st.write("Ladder pad width: ", round(width, 1))
