import streamlit as st
from graficas_plotly import exportaciones, fish

st.plotly_chart(exportaciones)
st.plotly_chart(fish)
