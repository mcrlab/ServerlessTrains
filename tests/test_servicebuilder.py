from lib.servicebuilder import ServiceBuilder
from lib.stationlist import StationList
import unittest
from unittest.mock import patch, call

mock_service_data = {
    "serviceID": "SERVICE_ID"
}

@patch.object(StationList, 'get_station_name', return_value="STATION_NAME")
class TestServiceBuilder(unittest.TestCase):

    def test_it_can_be_initialised(self, mock_get_station_name):
        builder = ServiceBuilder()
        assert builder is not None
    
    def test_it_has_a_build_function(self, mock_get_station_name):
        builder = ServiceBuilder()
        assert builder.build is not None

    def test_build_should_return_a_dictionary(self, mock_get_station_name):
        builder = ServiceBuilder()
        from_crs = "MAN"
        to_crs = "NMC"
        service = builder.build(mock_service_data, from_crs, to_crs)
        self.assertIsInstance(service, dict)
    
    def test_build_should_return_a_dictionary_with_a_service_id(self, mock_get_station_name):
        builder = ServiceBuilder()
        from_crs = "MAN"
        to_crs = "NMC"
        service = builder.build(mock_service_data, from_crs, to_crs)
        self.assertEqual(service['id'], "SERVICE_ID")
    
    def test_build_should_return_a_dictionary_with_an_origin(self, mock_get_station_name):
        builder = ServiceBuilder()
        from_crs = "MAN"
        to_crs = "NMC"
        service = builder.build(mock_service_data, from_crs, to_crs)
        self.assertIn("origin", service.keys())

    def test_build_should_return_a_dictionary_with_an_origin_crs(self, mock_get_station_name):
        builder = ServiceBuilder()
        from_crs = "MAN"
        to_crs = "NMC"
        service = builder.build(mock_service_data, from_crs, to_crs)
        self.assertEqual(service['origin']['crs'], from_crs)
    
    def test_build_should_return_a_dictionary_with_a_destination(self, mock_get_station_name):
        builder = ServiceBuilder()
        from_crs = "MAN"
        to_crs = "NMC"
        service = builder.build(mock_service_data, from_crs, to_crs)
        self.assertIn("destination", service.keys())

    def test_build_should_return_a_dictionary_with_a_destination_crs(self, mock_get_station_name):
        builder = ServiceBuilder()
        from_crs = "MAN"
        to_crs = "NMC"
        service = builder.build(mock_service_data, from_crs, to_crs)
        self.assertEqual(service['destination']['crs'], to_crs) 

    def test_build_should_use_station_list_to_find_station_name_for_both_from_and_to_crs(self, mock_get_station_name):
        builder = ServiceBuilder()
        from_crs = "MAN"
        to_crs = "NMC"
        service = builder.build(mock_service_data, from_crs, to_crs)
        mock_get_station_name.assert_has_calls([call(from_crs), call(to_crs)])
        self.assertEqual(service['origin']['name'], "STATION_NAME")
        self.assertEqual(service['destination']['name'], "STATION_NAME")