import streamlit as st

#Header
st.header('Yuni :sparkles:')
st.subheader('Plot')

c1, c2, c3, c4 = st.columns(4)

with c1:
  x = st.number_input('x',value=0)
with c2:
  operator = st.selectbox(
    'Operator',
    ('+', '-', 'x', ':'), key='k1')
with c3:
  y = st.number_input('y',value=0)
with c4:
  x + y = o
  x - y = p
  x * y = q
  x / y = r
  st.if(operator=='+')
    st.write('= ', o)
  st.if(operator=='-')
    st.write('= ', p)
  st.if(operator=='x')
    st.write('= ', q)
  st.if(operator==':')
    st.write('= ', r)

st.caption('Copyright © Yuni Setiasari 2023')
