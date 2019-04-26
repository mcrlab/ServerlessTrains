from lib.train import Train, Stop
import unittest
import pytest

class TestTrain(unittest.TestCase):
    
    def setUp(self):
        pass
       
    def tearDown(self):
        pass

    def test_it_can_be_initialised(self):
        assert Train is not None

    def test_scheduled_departure_time_from_origin(self):
        origin = Stop("NMC", "New Mills Central", 100, 200)
        destination = Stop("MAN", "Manchester", 200, 300)
        train = Train("ID", origin, destination, 1, False)
        
        departure_time = train.scheduled_departure_time()

        self.assertEqual(departure_time, 100) 

    def test_estimated_departure_time_from_origin(self):
        origin = Stop("NMC", "New Mills Central", 100, 200)
        destination = Stop("MAN", "Manchester", 200, 300)
        train = Train("ID", origin, destination, 1, False)
        
        departure_time = train.estimated_departure_time()

        self.assertEqual(departure_time, 200)

    def test_scheduled_arrival_time_from_destination(self):
        origin = Stop("NMC", "New Mills Central", 100, 200)
        destination = Stop("MAN", "Manchester", 200, 300)
        train = Train("ID", origin, destination, 1, False)
        
        arrival_time = train.scheduled_arrival_time()

        self.assertEqual(arrival_time, 200)  

    def test_estimated_arrival_time_from_destination(self):
        origin = Stop("NMC", "New Mills Central", 100, 200)
        destination = Stop("MAN", "Manchester", 200, 300)
        train = Train("ID", origin, destination, 1, False)
        
        arrival_time = train.estimated_arrival_time()

        self.assertEqual(arrival_time, 300)  


    
class TestStop(unittest.TestCase):
    def test_it_can_be_initialised(self):
        assert Stop is not None