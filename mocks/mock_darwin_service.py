from .mock import mock_service

class MockDarwinService():
    def __init__(self, wsdl, token):
        self.wsdl = wsdl
        self.token = token
        self.services = []

    def load_departures(self, from_crs, to_crs, number_of_departures):
        mock_services = []
        mock_services.append(mock_service)
        return mock_services