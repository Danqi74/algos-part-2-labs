import unittest

from scr.angry_cows import get_distance

class TestMaxMinDistance(unittest.TestCase):
    def test_get_distance_case1(self):
        self.assertEqual(get_distance(5, 3, [1, 2, 8, 4, 9]), 3)
    def test_get_distance_case2(self):
        self.assertEqual(get_distance(2, 2, [1, 2]), 0)
    def test_get_distance_case3(self):
        self.assertEqual(get_distance(7, 7, [1, 2, 3, 4, 5, 6, 7]), 0)
    def test_get_distance_case4(self):
        self.assertEqual(get_distance(5, 3, [1, 1, 1, 1, 1]), 0)
    def test_get_distance_case5(self):
        self.assertEqual(get_distance(5, 4, [1, 3, 7, 11, 15]), 4)
    def test_get_distance_case6(self):
        self.assertEqual(get_distance(8, 4, [3, 6, 2, 12, 8, 16, 10, 14]), 4)
    def test_get_distance_case7(self):
        self.assertEqual(get_distance(10, 5, [1_000_000_000, 500_000_000, 750_000_000, 250_000_000, 125_000_000, 375_000_000, 625_000_000, 875_000_000, 312_500_000, 687_500_000]), 187_500_000)
    def test_get_distance_case8(self):
        self.assertEqual(get_distance(4, 4, [1, 3, 5, 7]), 2)

if __name__ == '__main__':
    unittest.main()
