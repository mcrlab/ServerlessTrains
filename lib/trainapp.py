import zeep
from lib.trainfactory import TrainServiceFactory
import os

class TrainApp:
    def loadServices(self, fromCRS, toCRS):
        wsdl = os.environ['WSDL']
        token = os.environ['DARWIN_TOKEN']

        try:
            client = zeep.Client(wsdl=wsdl)
            response = client.service.GetDepartureBoard(numRows=2, crs=fromCRS, filterCrs=toCRS, timeOffset=0, timeWindow=120, _soapheaders={"AccessToken":token})
            return response

        except(zeep.exceptions.Fault):
            print("Exception")

    def fetchDeparturesForStation(self, fromCRS, toCRS):
        departures = []
        trainServiceFactory = TrainServiceFactory()

        response = self.loadServices(fromCRS, toCRS)
        location = {}
        location['name'] = response.locationName.replace("New Mills ", "")
        location['crs'] = response.crs

        if response.trainServices is not None:
            for serviceData in response.trainServices.service:
                trainService = trainServiceFactory.buildService(serviceData, location)
                departures.append(trainService)

        return departures
