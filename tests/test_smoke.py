'''
import unittest
from handler import iot, next, spread
from lib.darwinservice import DarwinService
from unittest.mock import patch
from mocks.mock_darwin_service import MockDarwinService
import pytest

class TestSmoke(unittest.TestCase):
    list_of_on_time_departures = MockDarwinService(False, False).load_departures(False, False, False)

    @patch.object(DarwinService, 'load_departures', return_value=list_of_on_time_departures)
    def test_iot_endpoint(self, load_departures):
        event = {
            "pathParameters": {
                "from": "NMC",
                "to" : "MAN"
            }
        }
        result = iot(event, False)   
        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(result['headers']['Access-Control-Allow-Origin'], '*')
        self.assertEqual(result['headers']['Access-Control-Allow-Credentials'], True)
        self.assertEqual(result['body'],1047)

    @patch.object(DarwinService, 'load_departures', return_value=list_of_on_time_departures)
    def test_next_endpoint(self, load_departures):
        event = { "pathParameters": { "from": "NMC", "to" : "MAN" } }
#        expected_json = '{"departures": [{"id": "WizqNi2tAjI+k2qo9FWauA==", "origin": {"crs": "NMC", "name": "New Mills Central", "scheduled": "17:27", "estimated": "17:27"}, "destination": {"crs": "MAN", "name": "Manchester Piccadilly", "scheduled": "17:58", "estimated": "17:58"}, "isCancelled": false, "platform": "2"}]}'
        expected_json = '{"departures": [{"id": "WizqNi2tAjI+k2qo9FWauA==", "origin": {"station": {"crs": "NMC", "name": "New Mills Central"}, "time": {"scheduled": "17:27", "estimated": "17:27"}}, "destination": {"station": {"crs": "MAN", "name": "Manchester Piccadilly"}, "time": {"scheduled": "17:58", "estimated": "17:58"}}, "isCancelled": false, "isDelayed": false, "platform": "2"}]}'
        result = next(event, False)   
        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(result['headers']['Access-Control-Allow-Origin'], '*')
        self.assertEqual(result['headers']['Access-Control-Allow-Credentials'], True)
        print(result['body'])
        self.assertEqual(result['body'],expected_json)


if __name__ == '__main__':
    unittest.main()
'''
