from lib.stationlist import StationList

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

    def get_arrival_time(self, service_data, destination_crs):
        calling_points = self.extract_calling_points(service_data);
        destination = self.extract_destination(calling_points, destination_crs)
        scheduled_time = destination['st']
        estimated_time = destination['et']
        estimated_time = self.calculate_estimated_time(scheduled_time, estimated_time)

        return scheduled_time, estimated_time
        
    def build(self, service_data, from_crs, to_crs):
        station_list = StationList()
        
        service = {}
        service['id'] = service_data['serviceID']
        service['origin'] = {}
        service['origin']['crs'] = from_crs
        service['origin']['name'] = station_list.get_station_name(from_crs)
        service['origin']['scheduled'] = service_data['std']
        service['origin']['estimated'] = self.calculate_estimated_time(service_data['etd'], service_data['std'])

        service['destination'] = {}
        service['destination']['crs'] = to_crs
        service['destination']['name'] = station_list.get_station_name(to_crs)
        service['destination']['scheduled'], service['destination']['estimated'] = self.get_arrival_time(service_data, to_crs)

        service['isCancelled'] = 0 if service_data['isCancelled'] is None else 1

        service['platform'] = self.extract_platform(service_data)

        return service