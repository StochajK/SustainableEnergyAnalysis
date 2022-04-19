"""
DS2001
Code for Final Project - Choropleth Map
7 April, 2022
choropleth.py
"""
# Import necessary libraries and packages
import json
import plotly.express as px
import plotly.io as pio
import pandas as pd
from energy_stat import EnergyStat

# Define necessary constants for files
ENERGY_JSON = "EnergyDataNew_EDITED.json"

def get_percent(partial_lst, total_lst):
    """ Function: get_percent
        Parameters: two lists containing EnergyStat objects
        Returns: one list of EnergyStat objects, with the amt value being the
                 percent of the amt value from the total list that the amt  
                 value from the partial list is
    """
    percent_lst = []
    
    for obj1 in total_lst:
        total = obj1.amt
        iso = obj1.country_code
        
        if obj1.amt != None and obj1.amt != 0:
            for obj2 in partial_lst:
                if obj2.country_code == iso:
                    if obj2.amt != None:
                        percent_lst.append(EnergyStat("Percent Renewable electricity "
                                                      "generation, " + obj2.country_name + 
                                                      ", Annual", (obj2.amt/total) * 100, iso))
                        break
                    else:
                        percent_lst.append(EnergyStat("Percent Renewable electricity "
                                                  "generation, " + obj2.country_name + 
                                                  ", Annual", None, iso))
                        break
        
        elif obj1.amt == 0:
            percent_lst.append(EnergyStat("Percent Renewable electricity "
                                          "generation, " + obj1.country_name + 
                                          ", Annual", 0, iso))
        
        else:
            percent_lst.append(EnergyStat("Percent Renewable electricity "
                                          "generation, " + obj1.country_name + 
                                          ", Annual", None, iso))
        
    return percent_lst

def main():
    # Read in the JSON file
    with open(ENERGY_JSON, "r") as infile:
        data = json.load(infile)
    
    # Construct empty lists for storing the energy objects
    renewable_energy_data = []
    total_energy_data = []
    
    # Create the EnergyStat objects and sort them based on its source
    for item in data:
        energy_obj = EnergyStat(item["name"], item["data"][0]["value"], 
                                item["iso"])
        if energy_obj.source == "Renewable electricity net generation":
            renewable_energy_data.append(energy_obj)
        elif energy_obj.source == "Electricity net generation":
            total_energy_data.append(energy_obj)
    
    # Calculate the percent energy produced that is renewable for each country 
    pct_data = get_percent(renewable_energy_data, total_energy_data)
    
    # Create the necessary lists for the pandas dataframe    
    pct_lst = [item.amt for item in pct_data]
    iso_lst = [item.country_code for item in pct_data]
    
    # Define the pandas dataframe
    d = {"iso": iso_lst, "REP": pct_lst}
    df = pd.DataFrame(data = d, index = [i for i in range(len(iso_lst))])
    
    # Define where the plot will be rendered and create the choropleth map
    pio.renderers.default = "browser"
    fig = px.choropleth(df, locations = "iso", locationmode = "ISO-3",
                    color="REP", color_continuous_scale = "greens")
    fig.show()
    
main()