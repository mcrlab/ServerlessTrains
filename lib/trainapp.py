import zeep
from lib.trainfactory import TrainServiceFactory
import os


class TrainApp:
    def __init__(self, darwin_service):
        self.darwin_service = darwin_service
        return

    def sort_departures(self, departures):
        return sorted(departures, key=lambda k:k['origin']['std'])

    def build_departures(self, response):
        return

    def fetch_departures(self, fromCRS, toCRS):
        departures = []

        response = self.darwin_service.load_departures(fromCRS, toCRS)

        if response.trainServices is not None:
            services = response.trainServices.service
            trainServiceFactory = TrainServiceFactory(fromCRS, toCRS, services)
            departures = trainServiceFactory.getDepartures()

        sorted_departures = self.sort_departures(departures)

        data = {
            "departures": sorted_departures
        }

        return data
