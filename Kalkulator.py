import streamlit as st

#Header
st.header('Yuni (210322607221) :sparkles:')
st.subheader('Plot')

c1, c2, c3, c4, c5 = st.columns(5)

with c1:
  x = st.number_input('Bilangan pertama',value=0)
with c2:
  operator = st.selectbox(
    'Operator',
    ('+', '-', 'x', ':'), key='k1')
with c3:
  y = st.number_input('Bilangan kedua',value=0)
with c4:
  if(operator=='+'):
    st.write('Hasil')
    st.write('= ', x+y)
  elif(operator=='-'):
    st.write('Hasil')
    st.write('= ', x-y)
  elif(operator=='x'):
    st.write('Hasil')
    st.write('= ', x*y)
  elif(operator==':'):
    st.write('Hasil')
    st.write('= ', x/y)
with c5:
  hasil = st.box(
    'Hasil',
    ('='), x+y)
st.caption('Copyright © Yuni Setiasari 2023')
