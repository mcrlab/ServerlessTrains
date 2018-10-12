import os
import json

class StationList:
    def __init__(self):
        data_string = open(os.environ['LAMBDA_TASK_ROOT']+'/lib/stations.json').read()
        data = json.loads(data_string)
        self.locations = data['locations'];

    def validateCRS(self, searchCRS):
        crs_list = [d['crs'] for d in self.locations]
        return searchCRS in crs_list

    def getStationName(self, searchCRS):
        station = next(item for item in self.locations if item["crs"] == searchCRS)
        return station['name']

    def stations(self):
        return self.locations
