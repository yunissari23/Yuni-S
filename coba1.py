import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Header
st.header('Yuni :sparkles:')
st.subheader('Plot')

x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y = np.sin(x) # Calculating sin(x) values
z = np.cos(x) # Calculating cos(x) values

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(x, y, label='sin(x)', color='b') # Plotting sin(x) curve
ax.plot(x, z, label='cos(x)', color='g') # Plotting cos(x) curve
ax.set_ylabel("")
ax.set_xlabel("x")
ax.tick_params(axis='y', labelsize=20)
ax.set_xticklabels(ax.get_xticklabels(), rotation=30, ha='right')
ax.tick_params(axis='x', labelsize=15)

st.pyplot(fig)
