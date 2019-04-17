import os
from .stationlist import StationList
from .servicebuilder import ServiceBuilder

class TrainApp:
    def __init__(self, darwin_service):
        self.darwin_service = darwin_service
        return

    def sort_departures(self, departures):
        return sorted(departures, key=lambda k:k['origin']['scheduled'])

    def next_departures(self, from_crs, to_crs, number_of_departures):
        station_list = StationList()
        if not station_list.validate_crs(from_crs) or not station_list.validate_crs(to_crs):
            raise Exception("CRS code is invalid")

        departures = []

        response = self.darwin_service.load_departures(from_crs, to_crs, number_of_departures)
  
        if response.trainServices is not None:
            for service_data in response.trainServices.service:
                train_service = ServiceBuilder().build(service_data, from_crs, to_crs)
                departures.append(train_service)

        return departures
