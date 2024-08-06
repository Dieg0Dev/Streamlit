import streamlit as st
import streamlit.components.v1 as components
import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network
import torneios 

st.title('Rede do Torneio')

#Network._repr_html_ = net_repr_html
st.sidebar.title('Selecione o Torneio de 2023 Aqui')
option=st.sidebar.selectbox('Selecione o Grand Slam',('Australian Open', 'Roland Garros', 'Wimblendom', 'US Open'))
physics=st.sidebar.checkbox('add physics interactivity?')

if option == 'Australian Open':
  torneios.ao_func(physics)
  HtmlFile = open("html_files/ao.html", 'r', encoding='utf-8')
  source_code = HtmlFile.read() 
  components.html(source_code, height = 1200,width=1000)
  
if option == 'Roland Garros':
  torneios.fo_func(physics)
  HtmlFile = open("html_files/fo.html", 'r', encoding='utf-8')
  source_code = HtmlFile.read() 
  components.html(source_code, height = 1200,width=1000)

if option == 'Wimblendom':
  torneios.wb_func(physics)
  HtmlFile = open("html_files/wb.html", 'r', encoding='utf-8')
  source_code = HtmlFile.read() 
  components.html(source_code, height = 1200,width=1000)
  
if option == 'US Open':
  torneios.uo_func(physics)
  HtmlFile = open("html_files/uo.html", 'r', encoding='utf-8')
  source_code = HtmlFile.read() 
  components.html(source_code, height = 1200,width=1000)