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
  st.if(operator=='+')
    st.write('= ', x+y)
  st.if(operator=='-')
    st.write('= ', x-y)
  st.if(operator=='x')
    st.write('= ', x*y)
  st.if(operator==':')
    st.write('= ', x/y)

st.caption('Copyright © Yuni Setiasari 2023')
