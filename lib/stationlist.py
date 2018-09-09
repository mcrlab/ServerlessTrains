import os
import json

class StationList:
    def __init__(self):
        data_string = open(os.environ['LAMBDA_TASK_ROOT']+'/lib/stations.json').read()
        data = json.loads(data_string)
        print(data)
        self.locations = data;

    def validateCRS(self, searchCRS):
        crs_list = [l['crs'] for l in self.locations]
        print(searchCRS)
        return searchCRS in crs_list
