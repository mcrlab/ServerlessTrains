
class ServiceListEncoder():

    def format_time(self, time):
        minutes = time % 60
        hours = int((time - minutes) / 60)
        return '{:02d}:{:02d}'.format(hours, minutes)  

    def to_json(self, services):
        data = []
        for service in services:
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
                    "name": service.destination.name,
                    "scheduled": self.format_time(service.scheduled_arrival_time()),
                    "estimated": self.format_time(service.estimated_arrival_time())
                },
                "isCancelled": service.is_cancelled(),
                "platform": service.platform
            }
            data.append(train)
        return data

class SimpleEncoder():
    def to_json(self, services):
        data = [];

        for index, service in enumerate(services):
            service = {
                "o" : service.origin.crs,
                "d" : service.destination.crs,
                "s" : service.scheduled_departure_time(),
                "e" : service.estimated_departure_time(),
            }
            data.append(service)
        return data