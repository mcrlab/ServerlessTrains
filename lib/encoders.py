import json
from lib.train import Time

class TimeEncoder(json.JSONEncoder):
    def default(self, time):
        if isinstance(time, Time):
            return [{
                "scheduled": time.scheduled 
            }]
        else:
            return super().default(time)


class ServiceListEncoder(json.JSONEncoder):


    def default(self, service):

        data = {
            "id": service.id,
            "isCancelled": 0,
            "platform": service.platform
        }
        return data
