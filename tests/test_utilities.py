import unittest
import pytest
from lib.utilities import build_response_object
from lib.utilities import extract_crs
from lib.utilities import time_to_integer
from lib.utilities import calculate_time

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


    def test_extract_crs_should_raise_if_event_dictionary_doesnt_contain_station(self):
        with pytest.raises(Exception) as e_info:
            event = {}
            from_crs, to_crs = extract_crs(event)

    def test_extract_crs_should_return_from_and_to_crs_from_event(self):
        event = { "pathParameters" : { "from" :"FROM", "to":"TO"}}
        from_crs, to_crs = extract_crs(event)
        self.assertEqual(from_crs, "FROM")
        self.assertEqual(to_crs, "TO")

    def test_extract_crs_should_return_from_and_to_crs_from_event_and_uppercase(self):
        event = { "pathParameters" : { "from" :"from", "to":"to"}}
        from_crs, to_crs = extract_crs(event)
        self.assertEqual(from_crs, "FROM")
        self.assertEqual(to_crs, "TO")


    def test_time_to_integer(self):
        time_string = "1:30"
        time_integer = time_to_integer(time_string)
        expected = 90
        self.assertEqual(time_integer, expected)

    def test_calculate_departure_time_should_return_scheduled_if_estimated_on_time(self):
        scheduled = "12:00"
        estimated = "On time"
        time = calculate_time(estimated, scheduled)
        self.assertEqual(time, "12:00")

    def test_calculate_departure_time_should_return_estimated_if_estimated_not_on_time(self):
        scheduled = "12:00"
        estimated = "12:01"
        time = calculate_time(estimated, scheduled)
        self.assertEqual(time, "12:01")

if __name__ == '__main__':
    unittest.main()
