from lib.servicebuilder import ServiceBuilder
from lib.stationlist import StationList
import unittest
from unittest.mock import patch, call
import pytest

mock_service_data = {
    "serviceID": "SERVICE_ID",
    "std": "12:00",
    "etd": "On time",
    "isCancelled": None,
    "platform": '1',
    'subsequentCallingPoints': {
        'callingPointList': [
            { 'callingPoint':[
                {
                    'locationName' :'TestStation',
                    'crs': 'NMC',
                    'st': '10:27',
                    'et': 'On time',
                    'at': None,
                    'isCancelled': None
                }
            ]}
        ]
    }
}

class TestServiceBuilder(unittest.TestCase):
    
    def setUp(self):
        self.builder = ServiceBuilder()
        self.from_crs = "MAN"
        self.to_crs = "NMC"
        self.patcher = patch.object(StationList,'get_station_name', return_value="STATION_NAME")
        self.mock_get_station_name = self.patcher.start()
       
    def tearDown(self):
        #self.patcher.stop()
        patch.stopall()

    def test_it_can_be_initialised(self):
        assert self.builder is not None
    
   
    # calculate_estimated_time
    def test_if_etd_is_on_time_then_etd_should_be_set_to_std(self):
        etd = "On time"
        std = "10:30"
        calculatedEtd = self.builder.calculate_estimated_time(etd, std)
        self.assertEqual(calculatedEtd, std)

    def test_if_etd_is_delayed_then_etd_should_remain_unchanged(self):
        etd = "10:40"
        std = "10:30"
        calculatedEtd = self.builder.calculate_estimated_time(etd, std)
        self.assertEqual(calculatedEtd, etd)


    # extract destination
    def test_extract_destination_should_match_on_the_destination_crs(self):
        calling_points = [ { "crs" : "ABC", "name": "test" }, ]
        destination_crs = "ABC"
        destination = self.builder.extract_destination(calling_points, destination_crs)
        self.assertEqual(destination['name'], "test")


    # calling points
    def test_get_calling_points_should_raise_exception_if_missing_calling_points(self):
        with pytest.raises(Exception) as e_info:
            service_data = {}
            self.builder.extract_calling_points(service_data)
    
    def test_get_calling_points_should_extract_calling_point_data_from_dictionary(self):
        service_data = {
            'subsequentCallingPoints': { 
                'callingPointList':[{'callingPoint':"DATA"}]
                }
            }
        calling_points = self.builder.extract_calling_points(service_data)
        self.assertEqual(calling_points, "DATA")



    # platform
    def test_extract_platform_from_service_data(self):
        platform = self.builder.extract_platform(mock_service_data)
        self.assertEqual(platform, "1")
    
    def test_extract_platform_from_service_missing(self):
        platform = self.builder.extract_platform({ 'platform': None})
        self.assertEqual(platform, "")


    


    