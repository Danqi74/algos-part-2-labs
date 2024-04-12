import unittest

from importmonkey import add_path

add_path("../src/")

from chess_knight import get_min_moves_count


class TestGetMinKnightMovesCount(unittest.TestCase):
    def test_with_base_8(self):
        board_size = "8"
        start_pos = "7, 0"
        destination_pos = "0, 7"
        expected_result = 6
        input_path = "test/input.txt"
        output_path = "test/output.txt"
        with open(input_path, "w") as file:
            file.writelines(board_size + "\n")
            file.writelines(start_pos + "\n")
            file.writelines(destination_pos)
        get_min_moves_count(input_path, output_path)
        with open(output_path, "r") as file:
            result = int(file.read())
        self.assertEqual(result, expected_result)

    def test_with_base_2(self):
        board_size = "2"
        start_pos = "0, 0"
        destination_pos = "1, 1"
        expected_result = -1
        input_path = "test/input.txt"
        output_path = "test/output.txt"
        with open(input_path, "w") as file:
            file.writelines(board_size + "\n")
            file.writelines(start_pos + "\n")
            file.writelines(destination_pos)
        get_min_moves_count(input_path, output_path)
        with open(output_path, "r") as file:
            result = int(file.read())
        self.assertEqual(result, expected_result)

    def test_with_base_4(self):
        board_size = "4"
        start_pos = "0, 0"
        destination_pos = "1, 1"
        expected_result = 4
        input_path = "test/input.txt"
        output_path = "test/output.txt"
        with open(input_path, "w") as file:
            file.writelines(board_size + "\n")
            file.writelines(start_pos + "\n")
            file.writelines(destination_pos)
        get_min_moves_count(input_path, output_path)
        with open(output_path, "r") as file:
            result = int(file.read())
        self.assertEqual(result, expected_result)

    def test_start_out_of_range(self):
        board_size = "6"
        start_pos = "7, 0"
        destination_pos = "0, 0"
        expected_result = -1
        input_path = "test/input.txt"
        output_path = "test/output.txt"
        with open(input_path, "w") as file:
            file.writelines(board_size + "\n")
            file.writelines(start_pos + "\n")
            file.writelines(destination_pos)
        get_min_moves_count(input_path, output_path)
        with open(output_path, "r") as file:
            result = int(file.read())
        self.assertEqual(result, expected_result)

    def test_destination_out_of_range(self):
        board_size = "6"
        start_pos = "0, 0"
        destination_pos = "7, 0"
        expected_result = -1
        input_path = "test/input.txt"
        output_path = "test/output.txt"
        with open(input_path, "w") as file:
            file.writelines(board_size + "\n")
            file.writelines(start_pos + "\n")
            file.writelines(destination_pos)
        get_min_moves_count(input_path, output_path)
        with open(output_path, "r") as file:
            result = int(file.read())
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
