import unittest

from src.word_chain import check_max_word_chain_length, read_input_file, write_output_file


class TestFilesOperations(unittest.TestCase):
    def setUp(self):
        self.input_path = "test/resources/wchain.in"
        self.output_path = "test/resources/wchain.out"
    
    def write_input_file(self, num_of_words, words):
        with open(self.input_path, "w", encoding="utf-8") as file:
            data = [word + "\n" for word in words]
            file.write(str(num_of_words)+ "\n")
            file.writelines(data)
    
    def read_output_file(self):
        with open(self.output_path, "r", encoding="utf-8") as file:
            result = file.read()
        return int(result)

    def test_read_input(self):
        num_of_words = 5
        words = ["a", "ab", "abd", "abcd", "aa"]
        self.write_input_file(num_of_words, words)
        self.assertEqual(read_input_file(self.input_path), (num_of_words, words))

    def test_write_output(self):
        result = 10
        write_output_file(self.output_path, result)
        self.assertEqual(self.read_output_file(), result)


class TestWordChainLength(unittest.TestCase):
    def setUp(self):
        self.input_path = "test/resources/wchain.in"
        self.output_path = "test/resources/wchain.out"
    
    def write_input_file(self, num_of_words, words):
        with open(self.input_path, "w", encoding="utf-8") as file:
            data = [word + "\n" for word in words]
            file.write(str(num_of_words)+ "\n")
            file.writelines(data)
    
    def read_output_file(self):
        with open(self.output_path, "r", encoding="utf-8") as file:
            result = file.read()
        return int(result)

    def test_example_1(self):
        num_of_words = 10
        words = ["crates", "car", "cats", "crate", "rate", "at", "ate", "tea", "rat", "a"]
        expected_result = 6
        self.write_input_file(num_of_words, words)
        check_max_word_chain_length(self.input_path, self.output_path)
        self.assertEqual(self.read_output_file(), expected_result)

    def test_example_2(self):
        num_of_words = 5
        words = ["b", "bcad", "bca", "bad", "bd"]
        expected_result = 4
        self.write_input_file(num_of_words, words)
        check_max_word_chain_length(self.input_path, self.output_path)
        self.assertEqual(self.read_output_file(), expected_result)

    def test_example_3(self):
        num_of_words = 3
        words = ["yetanotherword", "anotherword", "word"]
        expected_result = 1
        self.write_input_file(num_of_words, words)
        check_max_word_chain_length(self.input_path, self.output_path)
        self.assertEqual(self.read_output_file(), expected_result)

    def test_zero_words(self):
        num_of_words = 0
        words = []
        expected_result = 0
        self.write_input_file(num_of_words, words)
        check_max_word_chain_length(self.input_path, self.output_path)
        self.assertEqual(self.read_output_file(), expected_result)

    def test_incorrect_input(self):
        num_of_words = 2
        words = ["word"]
        expected_result = -1
        self.write_input_file(num_of_words, words)
        check_max_word_chain_length(self.input_path, self.output_path)
        self.assertEqual(self.read_output_file(), expected_result)


if __name__ == "__main__":
    unittest.main()
