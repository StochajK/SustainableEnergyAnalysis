"""
DS2001
Code for Final Project - Choropleth Map
7 April, 2022
choropleth.py
"""
# Import necessary libraries and packages
import json
import plotly.express as px
import pandas as pd
import kaleido
from energy_stat import EnergyStat

# Define necessary constants for files
ENERGY_JSON = "EnergyDataNew_EDITED.json"

def main():
    # Read in the JSON file
    with open(ENERGY_JSON, "r") as infile:
        data = json.load(infile)
    
    # Construct empty lists for storing the energy objects
    renewable_energy_data = []
    total_energy_data = []
    
    
    for item in data:
        energy_obj = EnergyStat(item["name"], item["data"][0]["value"], item["iso"])
        if energy_obj.source == "Renewable electricity net generation":
            renewable_energy_data.append(energy_obj)
        elif energy_obj.source == "Electricity net generation":
            total_energy_data.append(energy_obj)
    
    iso_lst = [item.country_code for item in renewable_energy_data]
    name_lst = [item.country_name for item in renewable_energy_data]
    renewable_eng_lst = [item.amt for item in renewable_energy_data]
    
    d = {"name": name_lst, "REP": renewable_eng_lst}
    df = pd.DataFrame(data = d, index = [i for i in range(len(iso_lst))])
    print(df)
    
    fig = px.choropleth(df, locations = "name", locationmode = "ISO-3",
                    color="REP",
                    color_continuous_scale=px.colors.sequential.Plasma)
    
    fig.show()
    # fig.write_image("images/fig1.png")
    
    
main()
