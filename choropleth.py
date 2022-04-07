"""
Kimberly Stochaj
DS2000
Code for Final Project - Choropleth Map
7 April, 2022
choropleth.py
"""
# Import necessary libraries and packages
import folium
import pandas as pd
import json
from folium import plugins
import plotly.express as px

# Define necessary constants for files
MAP = "countries.geojson"
ENERGY = "2019_global_energy_data.csv"

def main():
    """
    data = pd.read_json(MAP)
    print(data["features"][1]["properties"])
    """
    df = pd.read_csv(ENERGY)
    print(df)
    
    
    
main()
