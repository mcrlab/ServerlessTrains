import unittest
from lib.stationlist import StationList
from unittest.mock import patch, mock_open


data = '{ "locations": [ { "lat": 0.0, "lon": 0.0, "tiploc": "ALDRSJN", "name": "Aldershot North Junction", "crs": "ZAJ",  "toc": "SW" } ] }'
   
class TestStationList(unittest.TestCase):
    
    @patch("builtins.open", new_callable=mock_open, read_data=data)
    def test_get_stations_should_return_a_dictionary_of_locations(self, mock_file):
        station_list = StationList()
        assert len(station_list.stations()) == 1

    @patch("builtins.open", new_callable=mock_open, read_data=data)
    def test_get_station_name_should_return_a_station_name_from_a_crs(self, mock_file):
        station_list = StationList()
        station_name = station_list.get_station_name(search_crs="ZAJ")
        assert station_name == "Aldershot North Junction"

    @patch("builtins.open", new_callable=mock_open, read_data=data)
    def test_validate_crs_should_return_true_for_a_valid_crs(self, mock_file):
        station_list = StationList()
        crs_valid = station_list.validate_crs(search_crs="ZAJ")
        assert crs_valid == True

    @patch("builtins.open", new_callable=mock_open, read_data=data)
    def test_validate_crs_should_return_false_for_an_invalid_crs(self, mock_file):
        station_list = StationList()
        crs_valid = station_list.validate_crs(search_crs="AAA")
        assert crs_valid == False

    
if __name__ == '__main__':
    unittest.main()
