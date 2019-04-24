
class Train():
    def __init__(self,id, origin, destination, platform, cancelled = False):
        self.id = id
        self.origin = origin
        self.destination = destination
        self.platform = platform
        self.cancelled = cancelled

    def __str__(self):
        return self.id

    def is_cancelled(self):
        return self.cancelled

    
class Stop():
    def __init__(self, crs, name, time):
        self.crs = crs
        self.name = name
        self.time = time

    def __str__(self):
        return self.name


class Time():
    def __init__(self, secheduled, estimated):
        self.scheduled = secheduled
        self.estimated = estimated

    