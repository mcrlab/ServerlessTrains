
class Train():
    def __init__(self,id, origin, destination, platform, delayed = False, cancelled = False):
        self.id = id
        self.origin = origin
        self.destination = destination
        self.platform = platform
        self._delayed = delayed
        self._cancelled = cancelled


    def __str__(self):
        return self.id

    def scheduled_departure_time(self):
        return self.origin.time.scheduled

    def estimated_departure_time(self):
        return self.origin.time.estimated

    def scheduled_arrival_time(self):
        return self.destination.time.scheduled

    def estimated_arrival_time(self):
        return self.destination.time.estimated

    def is_delayed(self):
        return self._delayed

    def is_cancelled(self):
        return self._cancelled
    
class Stop():
    def __init__(self, station, time):
        self.station = station
        self.time = time

class Station():
    def __init__(self, crs, name):
        self.crs = crs
        self.name = name

    def __str__(self):
        return self.name

class Time():
    def __init__(self, scheduled, estimated):
        self.scheduled = scheduled
        self.estimated = estimated

    