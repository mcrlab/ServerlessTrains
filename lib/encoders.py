import json

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
                    "station" : service.origin.station.__dict__,
                    "time": service.origin.time.__dict__
                },
                "destination" : {
                    "station" : service.destination.station.__dict__,
                    "time": service.destination.time.__dict__
                },
                "isCancelled": service.is_cancelled(),
                "isDelayed": service.is_delayed(),
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