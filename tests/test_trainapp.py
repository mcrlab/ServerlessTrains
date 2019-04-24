import unittest
from lib.stationlist import StationList
from lib.trainapp import TrainApp
from lib.train import Train, Stop, Time
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
            Train("123",
                Stop("NMC", "New Mills Central", Time(100, 100)),
                Stop("MAN", "Manchester", Time(200, 200)),
                1
            ),
            Train("321",
                Stop("NMC", "New Mills Central", Time(50, 50)),
                Stop("MAN", "Manchester", Time(100, 100)),
                1
            )
        ]
        app = TrainApp(fake_darwin_service)
        sorted_departures = app.sort_departures(departures)
        self.assertEqual(sorted_departures[0].id, '321')


if __name__ == '__main__':
    unittest.main()
