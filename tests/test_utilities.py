import unittest
from lib.utilities import build_response_object
from lib.utilities import extract_CRS
from nose.tools import *

class TestUtilities(unittest.TestCase):

    def test_build_response_object_should_inject_status_code_and_body(self):
        status_code = 200
        body = "response text"
        expected = {
            "statusCode": 200,
            "headers": {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True,
            },
            "body": "response text"
        }
        response = build_response_object(status_code, body)
        self.assertEqual(response, expected)

    @raises(Exception)
    def test_extract_CRS(self):
        raise Exception("cheese")
        return

if __name__ == '__main__':
    unittest.main()
