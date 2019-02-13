import os
from .stationlist import StationList

def calculate_time(estimated, scheduled):
    if(estimated == "On time"):
        return scheduled
    else:
        return estimated

def get_calling_points(serviceData):
    return serviceData['subsequentCallingPoints']['callingPointList'][0]['callingPoint'];

def get_destination(callingPoints, destinationCRS):
    return next(item for item in callingPoints if item["crs"] == destinationCRS)

def get_arrival_time(service_data, destination_CRS):

    calling_points = get_calling_points(service_data);
    destination = get_destination(calling_points, destination_CRS)
    scheduled_time = destination['st']
    estimated_time = calculate_time(scheduled_time, destination['et'])

    return scheduled_time, estimated_time

def buildService(service_data, fromCRS, toCRS):
    stationList = StationList()
    originName = stationList.getStationName(fromCRS)
    destinationName = stationList.getStationName(toCRS)

    data = {}
    data['id'] = service_data.serviceID

    data['origin'] = {}
    data['origin']['name'] = originName
    data['origin']['crs'] = fromCRS
    data['origin']['std'] = service_data.std
    data['origin']['etd'] = calculate_time(service_data.etd, service_data.std)

    data['destination'] = {}
    data['destination']['name'] = destinationName
    data['destination']['crs'] = toCRS
    data['destination']['sta'], data['destination']['eta'] = get_arrival_time(service_data, toCRS)

    data['isCancelled'] = service_data.isCancelled

    if service_data.platform is not None:
        data['platform'] = service_data.platform
    else:
        data['platform'] = ""

    return data


class TrainApp:
    def __init__(self, darwin_service):
        self.darwin_service = darwin_service
        return

    def sort_departures(self, departures):
        return sorted(departures, key=lambda k:k['origin']['std'])

    def next_departures(self, from_crs, to_crs):
        departures = []

        response = self.darwin_service.load_departures(from_crs, to_crs)

        if response.trainServices is not None:
            for service_data in response.trainServices.service:
                train_service = buildService(service_data, from_crs, to_crs)
                departures.append(train_service)

        sorted_departures = self.sort_departures(departures)

        return sorted_departures
