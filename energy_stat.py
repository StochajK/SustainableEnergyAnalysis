"""
DS2001
Practicum project - creating a class to hold data used in cloropleth.py
16 April, 2022
energy_stat.py
"""

class EnergyStat:
    """ The EnergyStat class is a clean way of holding the important
        information retrieved from the JSON file that is needed to make the
        cloropleth map
    """
    def __init__(self, name_string, amt, code):
        """ constructor for an EnergyStat object
        """
        if type(amt) == float or type(amt) == int: 
            self.amt = float(amt)
        else:
            self.amt = None
        self.country_name, self.source = self.get_info(name_string)
        self.country_code = code
    
    def get_info(self, info_str):
        """ returns the country and the energy source from the provided string
            from the JSON file... string format is "source, country, period"
        """
        lst = info_str.split(",")
        return (lst[1], lst[0])
    
    def __str__(self):
        """ Reader friendly string version of an instance of this object"""
        return self.country_name + " produces " + str(self.amt) + " for " + self.source 
        
        
