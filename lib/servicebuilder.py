from lib.stationlist import StationList
from lib.utilities import calculate_time

class ServiceBuilder():
    def __init__(self):
        pass
    
    def build(self, service_data, from_crs, to_crs):
        station_list = StationList()
        
        service = {}
        service['id'] = service_data['serviceID']
        service['origin'] = {}
        service['origin']['crs'] = from_crs
        service['origin']['name'] = station_list.get_station_name(from_crs)
        service['origin']['scheduled'] = service_data['std']
        service['origin']['estimated'] = calculate_time(service_data['etd'], service_data['std'])

        service['destination'] = {}
        service['destination']['crs'] = to_crs
        service['destination']['name'] = station_list.get_station_name(to_crs)

        service['isCancelled'] = service_data['isCancelled']
        return service