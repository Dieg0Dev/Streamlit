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

def ao_func(physics):

    tennis_net = Network(height="500px", width="700px", bgcolor="#222222", font_color="white", directed=True)
    torneio = australian_open
    year = 2023

    torneio = torneio[torneio['Date'].dt.year == year]
    G = nx.DiGraph()

    for index, row in torneio.iterrows():
        player1 = row['Player_1']
        player2 = row['Player_2']
        winner = row['Winner']
        if player1 == winner: 
            G.add_edge(player1, player2)
        else:
            G.add_edge(player2, player1)
    tennis_net.from_nx(G)
    if physics:
        tennis_net.show_buttons(filter_=['physics'])
    tennis_net.write_html('html_files/ao.html')

def fo_func(physics):

    tennis_net = Network(height="500px", width="700px", bgcolor="#222222", font_color="white", directed=True)
    torneio = french_open
    year = 2023

    torneio = torneio[torneio['Date'].dt.year == year]
    G = nx.DiGraph()

    for index, row in torneio.iterrows():
        player1 = row['Player_1']
        player2 = row['Player_2']
        winner = row['Winner']
        if player1 == winner: 
            G.add_edge(player1, player2)
        else:
            G.add_edge(player2, player1)
    tennis_net.from_nx(G)
    if physics:
        tennis_net.show_buttons(filter_=['physics'])
    tennis_net.write_html('html_files/fo.html')
  
def wb_func(physics):

    tennis_net = Network(height="500px", width="700px", bgcolor="#222222", font_color="white", directed=True)
    torneio = wimbledon
    year = 2023

    torneio = torneio[torneio['Date'].dt.year == year]
    G = nx.DiGraph()

    for index, row in torneio.iterrows():
        player1 = row['Player_1']
        player2 = row['Player_2']
        winner = row['Winner']
        if player1 == winner: 
            G.add_edge(player1, player2)
        else:
            G.add_edge(player2, player1)
    tennis_net.from_nx(G)
    if physics:
        tennis_net.show_buttons(filter_=['physics'])
    tennis_net.write_html('html_files/wb.html')


def uo_func(physics):

    tennis_net = Network(height="500px", width="700px", bgcolor="#222222", font_color="white", directed=True)
    torneio = us_open
    year = 2023

    torneio = torneio[torneio['Date'].dt.year == year]
    G = nx.DiGraph()

    for index, row in torneio.iterrows():
        player1 = row['Player_1']
        player2 = row['Player_2']
        winner = row['Winner']
        if player1 == winner: 
            G.add_edge(player1, player2)
        else:
            G.add_edge(player2, player1)
    tennis_net.from_nx(G)
    if physics:
        tennis_net.show_buttons(filter_=['physics'])
    tennis_net.write_html('html_files/uo.html')