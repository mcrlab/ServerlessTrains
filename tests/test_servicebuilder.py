from lib.servicebuilder import ServiceBuilder
import unittest
from unittest.mock import patch

mock_service_data = {
    "serviceID": "SERVICE_ID"
}

class TestServiceBuilder(unittest.TestCase):
    def test_it_can_be_initialised(self):
        builder = ServiceBuilder()
        assert builder is not None
    
    def test_it_has_a_build_function(self):
        builder = ServiceBuilder()
        assert builder.build is not None

    def test_build_should_return_a_dictionary(self):
        builder = ServiceBuilder()
        from_crs = "MAN"
        service = builder.build(mock_service_data, from_crs)
        self.assertIsInstance(service, dict)
    
    def test_build_should_return_a_dictionary_with_a_service_id(self):
        builder = ServiceBuilder()
        from_crs = "MAN"
        service = builder.build(mock_service_data, from_crs)
        self.assertEqual(service['id'], "SERVICE_ID")
    
    def test_build_should_return_a_dictionary_with_an_origin(self):
        builder = ServiceBuilder()
        from_crs = "MAN"
        service = builder.build(mock_service_data, from_crs)
        self.assertIn("origin", service.keys())

    def test_build_should_return_a_dictionary_with_an_origin_crs(self):
        builder = ServiceBuilder()
        from_crs = "MAN"
        service = builder.build(mock_service_data, from_crs)
        self.assertEqual(service['origin']['crs'], from_crs)

    @patch('lib.stationlist.StationList')
    def test_what_is_going_on_with_patching(self, mock_station_list):
        mock_station_list.get_station_name.return_value = "STATION_NAME"

        self.assertEqual(mock_station_list.get_station_name(),"STATION_NAME")