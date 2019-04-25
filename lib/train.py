
class Train():
    def __init__(self,id, origin, destination, platform, cancelled = False):
        self.id = id
        self.origin = origin
        self.destination = destination
        self.platform = platform
        self.cancelled = cancelled

    def __str__(self):
        return self.id

    def scheduled_departure_time(self):
        return self.origin.scheduled_time

    def estimated_departure_time(self):
        return self.origin.estimated_time

    def scheduled_arrival_time(self):
        return self.destination.scheduled_time

    def estimated_arrival_time(self):
        return self.destination.estimated_time

    def is_cancelled(self):
        return self.cancelled
    
class Stop():
    def __init__(self, crs, name, scheduled_time, estimated_time):
        self.crs = crs
        self.name = name
        self.scheduled_time = scheduled_time
        self.estimated_time = estimated_time

    def __str__(self):
        return self.name


    