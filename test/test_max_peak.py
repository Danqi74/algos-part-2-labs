import unittest

from src.max_peak import get_max_peak


class TestPeaks(unittest.TestCase):
    def test_sorted_up(self):
        array = [1,4,8,15,26,68]
        self.assertEqual(get_max_peak(array),-1)
    def test_sorted_down(self):
        array = [94,54,48,30,11,8,-15]
        self.assertEqual(get_max_peak(array),-1)
    def test_two_elements(self):
        array = [156,0]
        self.assertEqual(get_max_peak(array),-1)
    def test_without_peaks(self):
        array = [15,2,16,19,20]
        self.assertEqual(get_max_peak(array),-1)
    def test_three_peaks(self):
        array = [0,15,16,25,-52,168,0,-3,-3,10,59,32]
        self.assertEqual(get_max_peak(array),5)

if __name__ == '__main__':
    unittest.main()
