import os
from .stationlist import StationList
from .servicebuilder import ServiceBuilder

class TrainApp:
    def __init__(self, darwin_service):
        self.darwin_service = darwin_service
        return

    def sort_departures(self, departures):
        return sorted(departures, key=lambda k:k.origin.time.scheduled)

    def next_departures(self, from_crs, to_crs, number_of_departures):
        station_list = StationList()
        if not station_list.validate_crs(from_crs) or not station_list.validate_crs(to_crs):
            raise Exception("CRS code is invalid")

        service_list = self.darwin_service.load_departures(from_crs, to_crs, number_of_departures)
        departures = []

        for service in service_list:
            train_service = ServiceBuilder().build_train(service, from_crs, to_crs)
            departures.append(train_service)

        return departures

    def multiple_departures(self, routes):
        departures = []
        
        for route in routes:
            origin = route['from']
            destination = route['to']
            new_departures_data = self.next_departures(origin, destination, 4)
            departures = departures + new_departures_data
        
        sorted_departures = self.sort_departures(departures)
        return sorted_departures