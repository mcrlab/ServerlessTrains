def calculate_etd(etd, std):
    if(etd == "On time"):
        return std
    else:
        return etd

def format_location(location):
    data = {}
    data['name'] = location.locationName
    data['crs'] = location.crs
    return data


class TrainServiceFactory():
    def init(self):
        return

    def buildService(self, serviceData, locationName):
        data = {}
        data['id'] = serviceData.serviceID
        data['origin'] = locationName
        data['destination'] = format_location(serviceData.destination.location[0])
        data['std'] = serviceData.std
        data['etd'] = calculate_etd(serviceData.etd, serviceData.std)
        data['isCancelled'] = serviceData.isCancelled
        return data
