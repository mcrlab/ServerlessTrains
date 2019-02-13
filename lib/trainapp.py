import zeep
from lib.trainfactory import TrainServiceFactory
import os


token = os.environ['DARWIN_TOKEN']


class TrainApp:
    def __init__(self, client):
        self.client = client
        return

    def load_services(self, fromCRS, toCRS):
        try:
            response = self.client.service.GetDepBoardWithDetails(numRows=4, crs=fromCRS, filterCrs=toCRS, timeOffset=0, timeWindow=120, _soapheaders={"AccessToken":token})
            return response

        except(zeep.exceptions.Fault):
            print("Exception")

    def sort_departures(self, departures):
        return sorted(departures, key=lambda k:k['origin']['std'])

    def build_departures(self, response):
        return

    def fetchDeparturesForStation(self, fromCRS, toCRS):
        departures = []

        response = self.load_services(fromCRS, toCRS)

        if response.trainServices is not None:
            services = response.trainServices.service
            trainServiceFactory = TrainServiceFactory(fromCRS, toCRS, services)
            departures = trainServiceFactory.getDepartures()

        sorted_departures = self.sort_departures(departures)

        data = {
            "departures": sorted_departures
        }
        
        return data
