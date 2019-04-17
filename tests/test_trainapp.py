import unittest
from lib.stationlist import StationList
from lib.trainapp import TrainApp

from unittest.mock import patch
import pytest

class TestTrainApp(unittest.TestCase):
    def test_setting_darwin_service(self):
        fake_darwin_service = {}
        app = TrainApp(fake_darwin_service)
        self.assertEqual(app.darwin_service, fake_darwin_service)
        
    def test_sort_departures(self):
        fake_darwin_service = {}
        departures = [
            { 
            'id': '123',
            'origin': {
                'scheduled' : '12:30'
                }
            },
                        { 
            'id': '321',
            'origin': {
                'scheduled' : '11:30'
                }
            },
        ]
        app = TrainApp(fake_darwin_service)
        sorted_departures = app.sort_departures(departures)
        self.assertEqual(sorted_departures[0]['id'], '321')


if __name__ == '__main__':
    unittest.main()
