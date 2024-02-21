import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def f(x):
  a = 19
  b = 1
  c = 18
  return a*x*x+b*x-c

x = st.slider('Pilih rentang', 0.0, 2.0, (.2, .5))
st.write('nilai x:', x)
y = st.slider('Set nilai', 0.0, 10.0, 6.0)
st.write('nilai y:', y)

t = np.linspace(x[0]*np.pi,x[1]*np.pi,100)
u = np.sin(y*t)
#st.write('nilai t:', t)

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(t, u, label='sin(t)', color='b') #Plotting sin(t) curve
ax.set_ylabel("")
ax.set_xlabel("t")
ax.tick_params(axis='y', labelsize=20)
ax.set_xticklabels(ax.get_xticklabels(), rotation=30, ha='right')
ax.tick_params(axis='x', labelsize=15)
plt.grid(color='green', linestyle='-.', linewidth=.5)
st.pyplot(fig)

#fungsi kuadrat dan integral
def f(x):
  a = 19
  b = 1
  c = 18
  return a*x*x+b*x-c

x = st.slider('Pilih rentang', -20, 20, (8, 12))
st.write('nilai x:', x)

t = np.linspace(x[0],x[1],100)
u = f(t)
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(t, u, label='sin(t)', color='b') #Plotting sin(t) curve
ax.set_ylabel("")
ax.set_xlabel("t")
ax.tick_params(axis='y', labelsize=20)
ax.set_xticklabels(ax.get_xticklabels(), rotation=30, ha='right')
ax.tick_params(axis='x', labelsize=15)
plt.grid(color='green', linestyle='-.', linewidth=.5)
st.pyplot(fig)
