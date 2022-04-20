"""
DS2001
Code for Final Project - Choropleth maps
7 April, 2022
choropleth.py
"""
# Import necessary libraries and packages
import json
import csv
import plotly.express as px
import plotly.io as pio
import pandas as pd
from energy_stat import EnergyStat

# Define necessary constants for files
ENERGY_JSON = "EnergyDataNew_EDITED.json"
GDP_CSV = "GDP_percapita_2019_fullworld.csv"

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

def create_choropleth(iso_lst, val_lst, val_str, title = "", 
                      color_scale = "blues", val_range = [0, 1]):
    """ Function: create_choropleth
        Parameters: iso_lst - a list of ISO country codes which corespond to
                              the built in GEOJSON in plotly express
                    val_lst - the values which the colors in the final 
                              choropleth map will be based on
                    val_str - a string used for the legend explaining what val
                              refers to
                    title - a string to be the title of the choropleth
                    color_scale - a string referring to a built in plotly 
                                  express continuous color gradient
                    val_range - a list containing the minimum and maximum
                                values for val
        Returns: Nothing, just renders a choropleth map in the browser window
    """
    # Create the Pandas data frame
    d = {"ISO" : iso_lst, val_str : val_lst}
    df = pd.DataFrame(data = d, index = [i for i in range(len(iso_lst))])
    
    # Render the choropleth map
    fig = px.choropleth(df, locations = "ISO", locationmode = "ISO-3", 
                       color = val_str, color_continuous_scale = color_scale,
                       range_color = val_range)
    fig.update_layout(title  = {"text": title,"x": 0.5, "xanchor": "center"})
    fig.show()
    

def main():
    # Define where plots are to be rendered
    pio.renderers.default = "browser"
    
    # For the clean energy production choropleth
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
    
    # Render the choropleth
    create_choropleth(iso_lst, pct_lst, "% Renewable Energy", 
                      title = "Percent of Total Energy Production that is Renewable by Country", 
                      color_scale = "greens", val_range = [0, 100])

    # For the GDP per capita choropleth
    # Read in the CSV file
    with open(GDP_CSV, "r") as infile:
        csvfile = csv.reader(infile, delimiter = ",")
        next(csvfile)
        
        # Construct empty lists to hold the ISOs and GDP per Capita values
        gdp_isos = []
        gdp_per_capita = []
    
        # Store the values from the CSVs in the lists
        for row in csvfile:
            if row[0] == "":
                break
            gdp_isos.append(row[3])
            if row[4] != "..":
                gdp_per_capita.append(float(row[4]))
            else:
                gdp_per_capita.append(None)
    
    # Render the GDP per capita choropleth
    create_choropleth(gdp_isos, gdp_per_capita, "GDP per capita", title = "GDP per Capita",
                      color_scale = "greens", val_range = [0, 90000])
        
    
main()