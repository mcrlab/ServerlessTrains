import unittest
from lib.trainapp import calculate_time
from lib.trainapp import get_destination
from lib.trainapp import get_calling_points
from nose.tools import *

class TestCalculateTime(unittest.TestCase):

    def test_if_etd_is_on_time_then_etd_should_be_set_to_std(self):
        etd = "On time"
        std = "10:30"
        calculatedEtd = calculate_time(etd, std)
        self.assertEqual(calculatedEtd, std)

    def test_if_etd_is_delayed_then_etd_should_remain_unchanged(self):
        etd = "10:40"
        std = "10:30"
        calculatedEtd = calculate_time(etd, std)
        self.assertEqual(calculatedEtd, etd)


class TestGetDestination(unittest.TestCase):
    def test_get_destination_should_match_on_the_destination_crs(self):
        calling_points = [ { "crs" : "ABC", "name": "test" }, ]
        destination_crs = "ABC"
        destination = get_destination(calling_points, destination_crs)
        self.assertEqual(destination['name'], "test")

class TestGetCallingPoints(unittest.TestCase):
    @raises(Exception)
    def test_get_calling_points_should_raise_exception_if_missing_calling_points(self):
        service_data = {}
        get_calling_points(service_data)
    
    def test_get_calling_points_should_extract_calling_point_data_from_dictionary(self):
        service_data = {
            'subsequentCallingPoints': { 
                'callingPointList':[{'callingPoint':"DATA"}]
                }
            }
        calling_points = get_calling_points(service_data)
        self.assertEqual(calling_points, "DATA")

if __name__ == '__main__':
    unittest.main()
