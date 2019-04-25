
class ServiceListEncoder():

    def format_time(self, time):
        minutes = time % 60
        hours = int((time - minutes) / 60)
        return '{:02d}:{:02d}'.format(hours, minutes)  

    def to_json(self, service_list):
        data = []
        for service in service_list:
            train = {
                "id": service.id,
                "origin" : {
                    "crs" : service.origin.crs,
                    "name": service.origin.name,
                    "scheduled": self.format_time(service.scheduled_departure_time()),
                    "estimated": self.format_time(service.estimated_departure_time())
                },
                "destination" : {
                    "crs" : service.destination.crs,
                    "name": service.origin.name,
                    "scheduled": self.format_time(service.scheduled_arrival_time()),
                    "estimated": self.format_time(service.scheduled_arrival_time())
                },
                "isCancelled": 0,
                "platform": service.platform
            }
            data.append(train)
        return data
