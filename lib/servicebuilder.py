from lib.stationlist import StationList
from lib.train import Train, Station, Stop, Time
from lib.utilities import time_to_integer

class ServiceBuilder():
    def calculate_estimated_time(self, estimated, scheduled):
        if(estimated == "On time"):
            return scheduled
        else:
            return estimated

    def extract_calling_points(self, service_data):
        try:
            return service_data['subsequentCallingPoints']['callingPointList'][0]['callingPoint']
        except KeyError:
            raise Exception("Failed to get calling points")

    def extract_destination(self, calling_points, destination_crs):
        return next(point for point in calling_points if point["crs"] == destination_crs)

    def extract_platform(self, service_data):
        return service_data['platform'] if service_data['platform'] is not None else ""

    def extract_cancelled(self, cancelled):
        return False if cancelled is None else True

    def extract_delayed(self, scheduled_departure_time, estimated_departure_time):
        return estimated_departure_time != scheduled_departure_time

    def get_arrival_time(self, service_data, destination_crs):
        calling_points = self.extract_calling_points(service_data)
        destination = self.extract_destination(calling_points, destination_crs)
        scheduled_time = destination['st']
        estimated_time = destination['et']
        estimated_time = self.calculate_estimated_time(scheduled_time, estimated_time)

        return scheduled_time, estimated_time
    
    def build_train(self, service_data, from_crs, to_crs):
        print(service_data)
        station_list = StationList()

        scheduled_departure_time = service_data['std']
        estimated_departure_time = self.calculate_estimated_time(service_data['etd'], service_data['std'])

        origin_station = Station(from_crs, station_list.get_station_name(from_crs))

        departure_time = Time(scheduled_departure_time, estimated_departure_time)

        origin = Stop(origin_station, departure_time)

        calling_points = self.extract_calling_points(service_data)
        destination = self.extract_destination(calling_points, to_crs)
        scheduled_arrival_time = destination['st']
        estimated_arrival_time = destination['et']
        estimated__arrival_time = self.calculate_estimated_time(scheduled_arrival_time, estimated_arrival_time)

        arrival_time = Time(scheduled_arrival_time, estimated__arrival_time)

        destination_station = Station(to_crs, 
                        station_list.get_station_name(to_crs)
                      )
                      
        destination = Stop(destination_station, arrival_time)

        platform = self.extract_platform(service_data)
        is_cancelled = self.extract_cancelled(service_data['isCancelled'])
        is_delayed = self.extract_delayed(scheduled_departure_time, estimated_departure_time)

        train = Train(
                    service_data['serviceID'],
                    origin,
                    destination,
                    platform,
                    is_delayed,
                    is_cancelled
                )
        return train
