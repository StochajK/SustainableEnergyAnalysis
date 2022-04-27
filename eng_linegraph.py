"""
DS2001
Code for final project - 
19 April 2022
eng_linegraph.py
"""
# Import necessary libraries
import json
import matplotlib.pyplot as plt
import csv
from energy_stat import EnergyStat

# Define necessary constants
ELECTRICITY_FILE = "OverTimeEnergyData.JSON"
GDP_FILE = "GDP_Percapita_1980_2020.csv"

def get_pct_change(lst):
    ''' Function: get_pct_change
        Parameters: a list from which the percent change between each
                    subsequent value is found
        Returns: a list of the percent change between each value of the 
                 origional list 
    '''
    pct_lst = []
    for i in range(len(lst) - 1):
        pct_change = ((lst[i + 1] - lst[i]) / lst[i]) * 100
        pct_lst.append(pct_change)
        
    return pct_lst

def make_plot(xvals, ylst1, ylst2, name):
    ''' Function: make_plot
        Parameters: xvals - a list to be the values on the x axis
                    ylst1 - a list to represent the y values for the first
                            series on the plot
                    ylst2 - a list to represent the y values for the second
                            series on the plot
                    name - the name of the country that the data refers to
        Returns: Nothing, just renders the graph to the plots pannel
    '''
    pct_lst1 = get_pct_change(ylst1)
    pct_lst2 = get_pct_change(ylst2)
    plt.plot(xvals, pct_lst1, label = "Renewable Energy Production")
    plt.plot(xvals, pct_lst2, label = "GDP per capita")
    plt.ylim(-50, 50)
    plt.yticks([(i - 5) * 10 for i in range(11)])
    plt.title("GDP per Capita and Renewable\n Energy Production for" + name)
    plt.xlabel("Year")
    plt.ylabel("% Change")
    plt.legend()
    plt.show()

def main():
    # Get data for GDP from JSON file
    with open(ELECTRICITY_FILE, "r") as infile:
        data = json.load(infile)
    
    # Make the empty lists to store the GDP data
    brazil_renewable = []
    iran_renewable = []
    norway_renewable = []
    usa_renewable = []
    
    lst_of_lsts = [brazil_renewable, iran_renewable, norway_renewable, usa_renewable]
    
    years = [i for i in range(1981, 2021)]
    
    # Sort through the JSON file, and organize the objects based on their country and source
    for item in data:
        for i in range(len(item["data"])):
            energy_obj = EnergyStat(item["name"], item["data"][i]["value"], 
                                    item["iso"])
            if energy_obj.country_code == "BRA":
                if energy_obj.source == "Renewable electricity net generation":
                    brazil_renewable.append(energy_obj)
            elif energy_obj.country_code == "IRN":
                if energy_obj.source == "Renewable electricity net generation":
                    iran_renewable.append(energy_obj)
            elif energy_obj.country_code == "NOR":
                if energy_obj.source == "Renewable electricity net generation":
                    norway_renewable.append(energy_obj)
            elif energy_obj.country_code == "USA":
                if energy_obj.source == "Renewable electricity net generation":
                    usa_renewable.append(energy_obj)
    
    gdp_lsts = []
    
    with open(GDP_FILE, "r") as infile:
        csvfile = csv.reader(infile, delimiter = ",")
        next(csvfile)
        i = 0
        for line in csvfile:
            if line[0] == "":
                break
            gdp_lsts.append(line[4:])
    
    gdp_lst_num = []
    
    for lst in gdp_lsts:
        nums = []
        for num in lst:
            nums.append(float(num))
        gdp_lst_num.append(nums)
                    
    lst_of_names = [lst[0].country_name for lst in lst_of_lsts]
    
    for i in range(len(lst_of_lsts)):
        make_plot(years, [item.amt for item in lst_of_lsts[i]], gdp_lst_num[i], lst_of_names[i])
    
main()
