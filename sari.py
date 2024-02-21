import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

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

#fungsi kuadrat
a = 25
b = 21
c = 14
n = 128

def f(x):
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

#metode trapesium integral
def trapesium(f, a, b, n=100):
  x = np.linspace(a, b, n+1)
  y = f(x)
  h = (b-a)/n
  s = 0.5*(y[0]+y[-1])+np.sum(y[1:-1])
  return h*s

#rentang integral
integral_range = st.slider('Pilih rentang', -20, 20, (4, 6), key='integral_range')
integral_result = trapesium(f, integral_range[0], integral_range[1])

#arsiran luas integral
t_fill = np.linspace(integral_range[0], integral_range[1], 100)
u_fill = f(t_fill)
ax.fill_between(t_fill, 0, u_fill, color='blue', alpha=0.4)

ax.set_xlabels("t")
plt.grid(color='green', linestyle='-.', linewidth=.5)
st.pyplot(fig)

st.write(f"Hasil integral pada rentang {integral_range} adalah: {integral_result}")
