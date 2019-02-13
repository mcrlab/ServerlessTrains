import zeep
from lib.trainfactory import TrainServiceFactory
import os

class TrainApp:
    def loadServices(self, fromCRS, toCRS):
        wsdl = os.environ['WSDL']
        token = os.environ['DARWIN_TOKEN']

        try:
            client = zeep.Client(wsdl=wsdl)
            response = client.service.GetDepBoardWithDetails(numRows=4, crs=fromCRS, filterCrs=toCRS, timeOffset=0, timeWindow=120, _soapheaders={"AccessToken":token})
            return response

        except(zeep.exceptions.Fault):
            print("Exception")

    def sortDepartures(self, departures):
        return sorted(departures, key=lambda k:k['origin']['std'])

    def fetchDeparturesForStation(self, fromCRS, toCRS):
        departures = []

        response = self.loadServices(fromCRS, toCRS)
        location = {}
        location['name'] = response.locationName
        location['crs']  = response.crs

        if response.trainServices is not None:
            services = response.trainServices.service
            trainServiceFactory = TrainServiceFactory(fromCRS, toCRS, services)
            departures = trainServiceFactory.getDepartures()

        sorted_departures = self.sortDepartures(departures)

        return sorted_departures
