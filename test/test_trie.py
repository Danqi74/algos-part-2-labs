import unittest

from importmonkey import add_path
add_path("../src/")

from trie import Trie, create_trie


class TestTrie(unittest.TestCase):
    def setUp(self):
        words = ["period", "person", "bell", "create", "machinery", "promised", "pure", "related"]
        self.trie = create_trie(words)

    def test_insert(self):
        self.assertFalse(self.trie.search("new"))
        self.trie.insert("new")
        self.assertTrue(self.trie.search("new"))

    def test_search_word(self):
        self.assertTrue(self.trie.search("bell"))
        self.assertTrue(self.trie.search("pure"))
        self.assertTrue(self.trie.search("person"))

        self.assertFalse(self.trie.search("child"))

    def test_search_prefix(self):
        self.assertTrue(self.trie.search_prefix("be"))
        self.assertTrue(self.trie.search_prefix("rel"))
        self.assertTrue(self.trie.search_prefix("per"))
        
        self.assertFalse(self.trie.search_prefix("chi"))

    def test_empty_searches(self):
        trie = Trie()
        self.assertFalse(trie.search("person"))
        self.assertFalse(trie.search("per"))


if __name__ == "__main__":
    unittest.main()
