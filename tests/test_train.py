from lib.train import Train, Stop
import unittest
import pytest

class TestTrain(unittest.TestCase):
    
    def setUp(self):
        pass
       
    def tearDown(self):
        pass

    def test_it_can_be_initialised(self):
        assert Train is not None
    
class TestStop(unittest.TestCase):
    def test_it_can_be_initialised(self):
        assert Stop is not None