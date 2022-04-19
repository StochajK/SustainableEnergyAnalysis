'''
    DS2001
    Group Project
    linegraph.py
'''

import seaborn as sns
import matplotlib.pyplot as plt
import csv
import numpy as np

GDP_FILE = "GDP_Percapita_1980_2020.csv"

def main():
    data = []
    brazil = []
    iran = []
    norway = []
    usa = []
    with open(GDP_FILE, "r") as infile:
        csvfile = csv.reader(infile, delimiter = ",")
        for row in csvfile:
            data.append(row)
            
        print(data)
                
        # print(data)
        
        # for gdp in data:
        #     brazil.append(float(data[1][4:]))
            
        # gdp = np.array(data[5:], dtype = float)
        # print(gdp)
        # # gdp = [float(i) for i in data[4:]]
        # brazil.append(float(data[1][4:]))
        # print(brazil)
        
        # #     # iran = iran.append(data[2][4:])
        # #     # norway = norway.append(data[3][4:])
        # #     # usa = usa.append(data[4][4:])
        # # # print(brazil)
        # # # print(data[1][4:])
        # # # print(data)
        # # print(data[0][4:])
        # # print(data[1][4:])
        # plt.plot(data[0][4:], data[1][4:])
        # print(float(data[1][4:]))
        
main()


