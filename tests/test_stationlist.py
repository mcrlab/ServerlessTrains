import unittest
from lib.stationlist import StationList
from unittest.mock import patch, mock_open
import json
from tests.data.mock_data import mock_locations
  
class TestStationList(unittest.TestCase):
    
    @patch("builtins.open", new_callable=mock_open, read_data=mock_locations)
    def test_load_stations_should_open_file_and_return_json(self, mock_file):
        station_list = StationList()
        stations = station_list.load_stations()
        assert len(station_list.stations()) == 1

    @patch.object(StationList, 'load_stations')
    def test_get_stations_should_call_load_stations(self, mock_load_stations):
        station_list = StationList()
        station_list.stations()
        mock_load_stations.assert_called()

    @patch.object(StationList, 'load_stations')
    def test_get_stations_should_return_a_dictionary_of_locations(self, mock_load_stations):
        mock_load_stations.return_value = json.loads(mock_locations)
        station_list = StationList()
        assert len(station_list.stations()) == 1


    @patch.object(StationList, 'load_stations')
    def test_get_station_name_should_return_a_station_name_from_a_crs(self, mock_load_stations):
        mock_load_stations.return_value = json.loads(mock_locations)['locations']
        station_list = StationList()
        station_name = station_list.get_station_name(search_crs="ZAJ")
        assert station_name == "Aldershot North Junction"

    @patch.object(StationList, 'load_stations')
    def test_validate_crs_should_return_true_for_a_valid_crs(self, mock_load_stations):
        mock_load_stations.return_value = json.loads(mock_locations)['locations']
        station_list = StationList()
        crs_valid = station_list.validate_crs(search_crs="ZAJ")
        assert crs_valid == True

    @patch.object(StationList, 'load_stations')
    def test_validate_crs_should_return_false_for_an_invalid_crs(self, mock_load_stations):

        mock_load_stations.return_value = json.loads(mock_locations)['locations']
        station_list = StationList()
        crs_valid = station_list.validate_crs(search_crs="AAA")
        assert crs_valid == False

    
if __name__ == '__main__':
    unittest.main()
