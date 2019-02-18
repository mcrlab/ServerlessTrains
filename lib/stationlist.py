import os
import json

class StationList:
    def __init__(self):
        self.locations = []

    def load_stations(self):
        data_string = open(os.path.join(os.path.dirname(__file__), '../data/stations.json')).read()
        data = json.loads(data_string)
        return data['locations']

    def validate_crs(self, search_crs):
        locations = self.load_stations()
        crs_list = [item['crs'] for item in locations]

        return search_crs in crs_list

    def get_station_name(self, search_crs):
        locations = self.load_stations()
        station = next(item for item in locations if item["crs"] == search_crs)
        return station['name']

    def stations(self):
        stations = self.load_stations()
        return stations
