import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network
import pandas as pd
import streamlit as st
from IPython.display import HTML, display


tennis_df = pd.read_csv("https://raw.githubusercontent.com/Dieg0Dev/datasets/main/atp_tennis.csv")
tennis_df['Date'] = pd.to_datetime(tennis_df['Date'], errors='coerce')

grand_slams = tennis_df[tennis_df['Series'] == 'Grand Slam']

australian_open = tennis_df[tennis_df['Tournament'] == 'Australian Open']
french_open = tennis_df[tennis_df['Tournament'] == 'French Open']
wimbledon = tennis_df[tennis_df['Tournament'] == 'Wimbledon']
us_open = tennis_df[tennis_df['Tournament'] == 'US Open']

tennis_net = Network(height="500px", width="700px", bgcolor="#222222", font_color="white", directed=True)
torneio = australian_open
year = 2023

torneio = torneio[torneio['Date'].dt.year == year]
torneio = torneio[torneio['Round'].str.contains('final', case=False, na=False)]

G = nx.DiGraph()

for index, row in torneio.iterrows():
    player1 = row['Player_1']
    player2 = row['Player_2']
    winner = row['Winner']
    if player1 == winner: 
        G.add_edge(player1, player2)
    else:
        G.add_edge(player2, player1)

def madj_func():

    tennis_net.from_nx(G)
    adj_matrix = nx.adjacency_matrix(G).todense()
    
    st.title("Visualização de Grafo Direcionado e Matriz de Adjacência")
    st.write("Matriz de Adjacência do Grafo:")
    st.write(pd.DataFrame(adj_matrix))
    
    path = "graph.html"
   
def dia_per_func():
    G_undirected = G.to_undirected()
    try:
        diameter = nx.diameter(G_undirected)
        st.write(f"Diâmetro do grafo direcionado (convertido para não direcionado): {diameter}")
    except nx.NetworkXError:
        st.write("O grafo não é conexo, então o diâmetro não pode ser calculado.")
        
    all_pairs_shortest_path_length = dict(nx.all_pairs_shortest_path_length(G_undirected))
    max_distances = {node: max(lengths.values()) for node, lengths in all_pairs_shortest_path_length.items()}
    max_distance = max(max_distances.values())
    periphery_nodes = [node for node, dist in max_distances.items() if dist == max_distance]
    st.write(f"Nós da periferia: {periphery_nodes}")
    

