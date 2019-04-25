from lib.stationlist import StationList
from lib.train import Train, Stop
from lib.utilities import time_to_integer

class ServiceBuilder():
    def __init__(self):
        pass

    def calculate_estimated_time(self, estimated, scheduled):
        if(estimated == "On time"):
            return scheduled
        else:
            return estimated

    def extract_calling_points(self, service_data):
        try:
            return service_data['subsequentCallingPoints']['callingPointList'][0]['callingPoint'];
        except KeyError as e:
            raise Exception("Failed to get calling points")

    def extract_destination(self, calling_points, destination_crs):
        return next(point for point in calling_points if point["crs"] == destination_crs)

    def extract_platform(self, service_data):
        return service_data['platform'] if service_data['platform'] is not None else ""

    def extract_cancelled(self, cancelled):
        return 0 if cancelled is None else 1

    def get_arrival_time(self, service_data, destination_crs):
        calling_points = self.extract_calling_points(service_data);
        destination = self.extract_destination(calling_points, destination_crs)
        scheduled_time = destination['st']
        estimated_time = destination['et']
        estimated_time = self.calculate_estimated_time(scheduled_time, estimated_time)

        return scheduled_time, estimated_time
    
    def build_train(self, service_data, from_crs, to_crs):
        station_list = StationList()
        scheduled_departure_time = time_to_integer(service_data['std'])
        estimated_departure_time = time_to_integer(self.calculate_estimated_time(service_data['etd'], service_data['std']))

        origin = Stop(from_crs, 
                        station_list.get_station_name(from_crs),
                        scheduled_departure_time, 
                        estimated_departure_time
                      )


        calling_points = self.extract_calling_points(service_data)
        destination = self.extract_destination(calling_points, to_crs)
        scheduled_time = destination['st']
        estimated_time = destination['et']
        estimated_time = self.calculate_estimated_time(scheduled_time, estimated_time)


        destination = Stop(to_crs, 
                        station_list.get_station_name(to_crs),
                        time_to_integer(scheduled_time), 
                        time_to_integer(estimated_time)
                      )

        train = Train(
                    service_data['serviceID'],
                    origin,
                    destination,
                    self.extract_platform(service_data),
                    False if service_data['isCancelled'] is None else True
                )
        return train
