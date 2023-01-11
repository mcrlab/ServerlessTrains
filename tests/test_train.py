from lib.train import Train, Stop, Time
import unittest
import pytest

class TestTrain(unittest.TestCase):
    
    def setUp(self):
        pass
       
    def tearDown(self):
        pass

    def test_it_can_be_initialised(self):
        assert Train is not None

    @pytest.mark.skip(reason="no way of currently testing this")
    def test_scheduled_departure_time_from_origin(self):
        origin = Stop("NMC", "New Mills Central")
        departure = Time(100, 200)
        destination = Stop("MAN", "Manchester")
        arrival = Time(200, 300)
        train = Train("ID", origin, destination, departure, arrival, 1, False)
        
        departure_time = train.scheduled_departure_time()

        self.assertEqual(departure_time, 100) 

    @pytest.mark.skip(reason="no way of currently testing this")
    def test_estimated_departure_time_from_origin(self):
        origin = Stop("NMC", "New Mills Central")
        departure = Time(100, 200)
        destination = Stop("MAN", "Manchester")
        arrival = Time(200, 300)
        train = Train("ID", origin, destination, departure, arrival, 1, False)
        
        departure_time = train.estimated_departure_time()

        self.assertEqual(departure_time, 200)

    @pytest.mark.skip(reason="no way of currently testing this")
    def test_scheduled_arrival_time_from_destination(self):
        origin = Stop("NMC", "New Mills Central")
        departure = Time(100, 200)
        destination = Stop("MAN", "Manchester")
        arrival = Time(200, 300)
        train = Train("ID", origin, destination, departure, arrival, 1, False)
        
        arrival_time = train.scheduled_arrival_time()

        self.assertEqual(arrival_time, 200)  

    @pytest.mark.skip(reason="no way of currently testing this")
    def test_estimated_arrival_time_from_destination(self):
        origin = Stop("NMC", "New Mills Central")
        departure = Time(100, 200)
        destination = Stop("MAN", "Manchester")
        arrival = Time(200, 300)
        train = Train("ID", origin, destination, departure, arrival, 1, False)
        
        arrival_time = train.estimated_arrival_time()

        self.assertEqual(arrival_time, 300)  

    @pytest.mark.skip(reason="no way of currently testing this")
    def test_is_cancelled(self):
        origin = Stop("NMC", "New Mills Central")
        departure = Time(100, 200)
        destination = Stop("MAN", "Manchester")
        arrival = Time(200, 300)

        cancelled_train =Train("ID", origin, destination, departure, arrival, 1, False, True)
        non_cancelled_train =Train("ID", origin, destination, departure, arrival, 1, False, False)

        self.assertTrue(cancelled_train.is_cancelled())
        self.assertFalse(non_cancelled_train.is_cancelled())
    
class TestStop(unittest.TestCase):
    def test_there_class_stop(self):
        assert Stop is not None
    @pytest.mark.skip(reason="no way of currently testing this")
    def test_stop_initialises_correctly(self):
        stop = Stop("NMN", "New Mills Newtown")
        self.assertEqual(stop.crs, "NMN")
        self.assertEqual(stop.name, "New Mills Newtown")
        