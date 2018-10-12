import json
from .stationlist import StationList

def calculate_time(estimated, scheduled):
    if(estimated == "On time"):
        return scheduled
    else:
        return estimated

def format_location(location):
    data = {}
    data['name'] = location.locationName
    data['crs'] = location.crs
    return data

def get_arrival_time(serviceData, destinationCRS):
    scheduled = ""
    estimated = ""
    try:
        callingPoints = serviceData['subsequentCallingPoints']['callingPointList'][0]['callingPoint'];
        destination = next(item for item in callingPoints if item["crs"] == destinationCRS)
        scheduled = destination['st']
        estimated = calculate_time(scheduled, destination['et'])
    except Exception as e:
        print(e)
    finally:
       return scheduled, estimated

class TrainServiceFactory():
    def __init__(self, fromCRS, toCRS, services):
        self.fromCRS = fromCRS
        self.toCRS = toCRS
        self.services = services
        self.stationList = StationList()

    def getDepartures(self):
        departures = []
        for serviceData in self.services:
            trainService = self.buildService(serviceData)
            departures.append(trainService)
        return departures

    def buildService(self, serviceData):

        originName = self.stationList.getStationName(self.fromCRS)
        destinationName = self.stationList.getStationName(self.toCRS)

        data = {}
        data['id'] = serviceData.serviceID

        data['origin'] = {}
        data['origin']['name'] = originName
        data['origin']['crs'] = self.fromCRS
        data['origin']['std'] = serviceData.std
        data['origin']['etd'] = calculate_time(serviceData.etd, serviceData.std)

        data['destination'] = {}
        data['destination']['name'] = destinationName
        data['destination']['crs'] = self.toCRS
        data['destination']['sta'], data['destination']['eta'] = get_arrival_time(serviceData, self.toCRS)

        data['isCancelled'] = serviceData.isCancelled
        if serviceData.platform is not None:
            data['platform'] = serviceData.platform
        else:
            data['platform'] = ""
        return data
