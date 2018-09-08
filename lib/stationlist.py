import os
import json

class StationList:
    def __init__(self):
        data_string = open(os.path.dirname(os.path.abspath(__file__))+'/stations.json').read()
        data = json.loads(data_string)
        self.locations = data['locations']

    def validateCRS(self, searchCRS):
        crs_list = [l['crs'] for l in self.locations]
        return searchCRS in crs_list
