"""
Kimberly Stochaj
DS2001
Code for final project - 
24 April, 2022
global_scatter.py
"""
# Import necessary libraries
import matplotlib.pyplot as plt
import json
import csv
import time

# Import necessary custom classes
from energy_stat import EnergyStat

# Define necessary constants
ENERGY_JSON = "GlobalEnergy_19802020.JSON"
GDP_CSV = "GDP_percapita.csv"

def make_scatter(x_vals, y_vals, title_lst, i):
    """ Function: make_scatter
        Parameters: x_vals - a dictionary where the keys are ISO country codes,
                             and the values are a list of floats to be used as 
                             the point's x value
                    y_vals - a dictionary where the keys are ISO country codes,
                             and the values are a list of floats to be used as 
                             the point's y value
                    title_lst - a list of the same length of the value list of
                                the prior dictionaries. Will be used to make
                                the graphs' title
                    i - an integer to indicate what index of all the lists to
                        utilize
        Returns: nothing, just renders the plot
    """
    plt.show()
    plt.title(title_lst[i])
    plt.xlabel("GDP per capita (constant 2015 USD)")
    plt.ylabel("Net Renewable Energy Generation (billion kWh)")
    plt.xlim([0, 100000])
    plt.ylim([0, 800])
    for key, value in x_vals.items():
        if key in y_vals:
            if x_vals[key][i] != None and y_vals[key][i].amt != None:
                plt.plot(x_vals[key][i], y_vals[key][i].amt, "o", color = "green")
    time.sleep(0.25)
    

def main():
    # Read in the energy JSON file
    with open(ENERGY_JSON, "r") as infile:
        data = json.load(infile)
        
    years = [i for i in range(1980, 2021)]
    
    dict_of_englsts = {}
    
    for item in data:
        for i in range(len(item["data"])):
            energy_obj = EnergyStat(item["name"], item["data"][i]["value"], 
                                    item["iso"])
            if energy_obj.country_code in dict_of_englsts:
                dict_of_englsts[energy_obj.country_code].append(energy_obj)
                
            else: 
                dict_of_englsts[energy_obj.country_code] = [energy_obj]
    
    # Read in the GDP csv file
    dict_of_gdplsts = {}
    
    with open(GDP_CSV, "r") as infile:
        csvfile = csv.reader(infile, delimiter = ",")
        next(csvfile)
        
        for line in csvfile:
            dict_of_gdplsts[line[1]] = line[24:]
    
    for key, value in dict_of_gdplsts.items():
        nums = []
        for num in value:
            if num == "":
                nums.append(None)
            else:
                nums.append(float(num))
        dict_of_gdplsts[key] = nums
    
    for i in range(len(years)):
        make_scatter(dict_of_gdplsts, dict_of_englsts, years, i)
    
    
main()