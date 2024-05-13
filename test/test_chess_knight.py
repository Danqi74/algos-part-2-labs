import unittest

from src.chess_knight import get_min_moves_count


class TestGetMinKnightMovesCount(unittest.TestCase):
    def setUp(self):
        self.input_path = "test/resources/input.txt"
        self.output_path = "test/resources/output.txt"

    def test_with_base_8(self):
        board_size = "8"
        start_pos = "7, 0"
        destination_pos = "0, 7"
        expected_result = 6
        with open(self.input_path, "w") as file:
            file.writelines(board_size + "\n")
            file.writelines(start_pos + "\n")
            file.writelines(destination_pos)
        get_min_moves_count(self.input_path, self.output_path)
        with open(self.output_path, "r") as file:
            result = int(file.read())
        self.assertEqual(result, expected_result)

    def test_with_base_2(self):
        board_size = "2"
        start_pos = "0, 0"
        destination_pos = "1, 1"
        expected_result = -1
        with open(self.input_path, "w") as file:
            file.writelines(board_size + "\n")
            file.writelines(start_pos + "\n")
            file.writelines(destination_pos)
        get_min_moves_count(self.input_path, self.output_path)
        with open(self.output_path, "r") as file:
            result = int(file.read())
        self.assertEqual(result, expected_result)

    def test_with_base_4(self):
        board_size = "4"
        start_pos = "0, 0"
        destination_pos = "1, 1"
        expected_result = 4
        with open(self.input_path, "w") as file:
            file.writelines(board_size + "\n")
            file.writelines(start_pos + "\n")
            file.writelines(destination_pos)
        get_min_moves_count(self.input_path, self.output_path)
        with open(self.output_path, "r") as file:
            result = int(file.read())
        self.assertEqual(result, expected_result)

    def test_start_out_of_range(self):
        board_size = "6"
        start_pos = "7, 0"
        destination_pos = "0, 0"
        expected_result = -1
        with open(self.input_path, "w") as file:
            file.writelines(board_size + "\n")
            file.writelines(start_pos + "\n")
            file.writelines(destination_pos)
        get_min_moves_count(self.input_path, self.output_path)
        with open(self.output_path, "r") as file:
            result = int(file.read())
        self.assertEqual(result, expected_result)

    def test_destination_out_of_range(self):
        board_size = "6"
        start_pos = "0, 0"
        destination_pos = "7, 0"
        expected_result = -1
        with open(self.input_path, "w") as file:
            file.writelines(board_size + "\n")
            file.writelines(start_pos + "\n")
            file.writelines(destination_pos)
        get_min_moves_count(self.input_path, self.output_path)
        with open(self.output_path, "r") as file:
            result = int(file.read())
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
