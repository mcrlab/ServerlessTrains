import zeep

class DarwinService():
    def __init__(self, wsdl, token):
        self.wsdl = wsdl
        self.token = token
        return

    def load_departures(self, from_crs, to_crs, number_of_departures):
        try:
            client = zeep.Client(self.wsdl)
            response = client.service.GetDepBoardWithDetails(numRows=number_of_departures,
                                                            crs=from_crs,
                                                            filterCrs=to_crs,
                                                            timeOffset=0,
                                                            timeWindow=120,
                                                            _soapheaders={"AccessToken":self.token})
            return response

        except(zeep.exceptions.Fault):
            print("Exception")
