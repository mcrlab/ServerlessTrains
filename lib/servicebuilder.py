class ServiceBuilder():
    def __init__(self):
        pass
    
    def build(self, service_data, from_crs):
        service = {}
        service['id'] = service_data['serviceID']
        service['origin'] = {}
        service['origin']['crs'] = from_crs

        return service