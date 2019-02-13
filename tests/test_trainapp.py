import unittest
from lib.trainapp import calculate_time

class TestCalculateTime(unittest.TestCase):

    def test_if_etd_is_on_time_then_etd_should_be_set_to_std(self):
        etd = "On time"
        std = "10:30"
        calculatedEtd = calculate_time(etd, std)
        self.assertEqual(calculatedEtd, std)

    def test_if_etd_is_not_on_time_then_etd_should_be_whatever_time_is_passed(self):
        etd = "12:30"
        std = "12:20"
        calculatedEtd = calculate_time(etd, std)
        self.assertEqual(calculatedEtd, etd)


if __name__ == '__main__':
    unittest.main()
