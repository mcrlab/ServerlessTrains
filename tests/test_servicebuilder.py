from lib.servicebuilder import ServiceBuilder
import unittest

class TestServiceBuilder(unittest.TestCase):
    def test_it_can_be_initialised(self):
        builder = ServiceBuilder()
        assert builder is not None
    
    def test_it_has_a_build_function(self):
        builder = ServiceBuilder()
        assert builder.build is not None