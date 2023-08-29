from lib.train import Train, Stop, Time, Station
import unittest
import pytest

class TestTrain(unittest.TestCase):
    
    def setUp(self):
        origin_station = Station("NMC", "New Mills Central")
        departure_time = Time(100, 200)
        origin = Stop(origin_station, departure_time)

        destination_station = Station("MAN", "Manchester")
        arrival_time = Time(200, 300)
        destination = Stop(destination_station, arrival_time)
        platform = 1

        self.train = Train("ID", origin, destination, platform, False, False)
        self.cancelled_train = Train("ID", origin, destination, platform, False, True)
        self.delayed_train = Train("ID", origin, destination, platform, True, False)
       
    def tearDown(self):
        pass

    def test_it_can_be_initialised(self):
        assert Train is not None

    def test_scheduled_departure_time_from_origin(self):
        departure_time =self. train.scheduled_departure_time()
        self.assertEqual(departure_time, 100) 

    def test_estimated_departure_time_from_origin(self):
        departure_time = self.train.estimated_departure_time()
        self.assertEqual(departure_time, 200)


    def test_scheduled_arrival_time_from_destination(self):   
        arrival_time = self.train.scheduled_arrival_time()

        self.assertEqual(arrival_time, 200)  

    def test_estimated_arrival_time_from_destination(self):        
        arrival_time = self.train.estimated_arrival_time()

        self.assertEqual(arrival_time, 300)  

    def test_is_cancelled(self):
        self.assertTrue(self.cancelled_train.is_cancelled())
        self.assertFalse(self.train.is_cancelled())

    def test_is_delayed(self):
        self.assertFalse(self.cancelled_train.is_delayed())
        self.assertFalse(self.train.is_delayed())
        self.assertTrue(self.delayed_train.is_delayed())
        
    
class TestStation(unittest.TestCase):
    def test_there_class_station(self):
        assert Station is not None
    
    def test_station_initialises_correctly(self):
        station = Station("NMN", "New Mills Newtown")
        self.assertEqual(station.crs, "NMN")
        self.assertEqual(station.name, "New Mills Newtown")
        