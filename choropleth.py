"""
Kimberly Stochaj
DS2000
Code for Final Project - Choropleth Map
7 April, 2022
choropleth.py
"""
# Import necessary libraries and packages
import json
# import plotly.express as px
# import pandas as pd
from energy_stat import EnergyStat

# Define necessary constants for files
ENERGY_JSON = "EnergyDataNew.json"

def main():
    # Read in the JSON file
    with open(ENERGY_JSON, "r") as infile:
        data = json.load(infile)
    
    # Construct empty lists for storing the energy objects
    renewable_energy_data = []
    total_energy_data = []
    
    
    for item in data:
        if type(item["data"][0]["value"]) == float:
            energy_obj = EnergyStat(item["name"], item["data"][0]["value"], item["iso"])
        else:
            energy_obj = EnergyStat(item["name"], "Nan", item["iso"])
        
        if energy_obj.source == "Renewable electricity net generation":
            renewable_energy_data.append(energy_obj)
        elif energy_obj.source == "Electricity net generation":
            total_energy_data.append(energy_obj)
            
    for country in total_energy_data:
        print(country)
        
        
    '''
    print(data[0]["name"])
    energy_example = EnergyStat(data[0]["name"], data[0]["data"][0]["value"], data[0]["iso"])
    print("Source =", energy_example.source)
    print("Country =", energy_example.country_name)
    print("Amount =", energy_example.amt)
    print("Code =", energy_example.country_code)
    '''
    
    
main()
