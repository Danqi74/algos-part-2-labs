import unittest

from src.flowers_store import get_max_flow, create_graph


class TestGraphCreation(unittest.TestCase):
    def test_creation(self):
        csv_data = """A
B
A,B,10
A,C,13
B,C,6
C,D,23
D,A,2"""
        input_path = "test/resources/input.csv"
        expected_result = {'A': {'B': 10, 'C': 13}, 'B': {'C': 6}, 'C': {'D': 23}, 'D': {'A': 2}}, 'A', 'B'

        with open(input_path, "w") as file:
            file.write(csv_data)

        result = create_graph(input_path)
        self.assertEqual(result, expected_result)



class TestMaxFlow(unittest.TestCase):
    def test_without_virtual_points(self):
        csv_data = """A
F
A,B,7
A,C,4
B,C,4
B,E,2
C,E,8
C,D,4
E,D,4
E,F,5
D,F,12"""
        input_path = "test/resources/input.csv"
        expected_result = 10

        with open(input_path, "w") as file:
            file.write(csv_data)

        result = get_max_flow(input_path)
        self.assertEqual(result, expected_result)

    def test_without_path(self):
        csv_data = """A
M
A,B,7
A,C,4
"""
        input_path = "test/resources/input.csv"
        expected_result = 0

        with open(input_path, "w") as file:
            file.write(csv_data)

        result = get_max_flow(input_path)
        self.assertEqual(result, expected_result)

    def test_with_virtual_points(self):
        csv_data = """A,B
F,G,H
A,C,3
A,D,9
C,F,5
D,F,7
D,G,4
F,G,11
D,B,40
B,E,13
E,D,18
E,H,5
"""
        input_path = "test/resources/input.csv"
        expected_result = 19

        with open(input_path, "w") as file:
            file.write(csv_data)

        result = get_max_flow(input_path)
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
