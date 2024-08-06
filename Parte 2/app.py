import streamlit as st
import streamlit.components.v1 as components
import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network
import analises 

st.title('Rede do Torneio')

st.sidebar.title('Selecione a Análise Aqui')
option=st.sidebar.selectbox('Análise:',('Matriz de Adj.', 'Diâmetro e Periferia da rede'))

if option == 'Matriz de Adj.':
  analises.madj_func()
  
if option == 'Diâmetro e Periferia da rede':
  analises.dia_per_func()
  
