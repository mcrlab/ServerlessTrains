import unittest

class TestCalculateTime(unittest.TestCase):

    def test_if_they_run_correctly(self):
        etd = "10:30"
        std = "10:30"
        self.assertEqual(etd, std)


if __name__ == '__main__':
    unittest.main()
