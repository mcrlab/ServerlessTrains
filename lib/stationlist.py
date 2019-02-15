import os
import json

class StationList:
    def __init__(self):
        data_string = open(os.path.join(os.path.dirname(__file__), '../data/stations.json')).read()
        data = json.loads(data_string)
        self.locations = data['locations']

    def validate_crs(self, search_crs):
        crs_list = [item['crs'] for item in self.locations]

        return search_crs in crs_list

    def get_station_name(self, search_crs):
        station = next(item for item in self.locations if item["crs"] == search_crs)
        return station['name']

    def stations(self):
        return self.locations
