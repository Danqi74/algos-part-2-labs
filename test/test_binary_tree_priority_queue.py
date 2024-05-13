import unittest

from src.binary_tree_priority_queue import PriorityQueue


class TestPriorityQueue(unittest.TestCase):
    def test_insert(self):
        queue = PriorityQueue()
        queue.insert("SomeTask 1", 5)
        queue.insert("SomeTask 2", 8)
        queue.insert("SomeTask 3", 3)
        queue.insert("SomeTask 4", 10)
        queue.insert("SomeTask 5", 9)
        queue.insert("SomeTask 6", 4)
        queue.insert("SomeTask 7", 1)
        expected_queue = [
            ("SomeTask 4", 10),
            ("SomeTask 5", 9),
            ("SomeTask 2", 8),
            ("SomeTask 1", 5),
            ("SomeTask 6", 4),
            ("SomeTask 3", 3),
            ("SomeTask 7", 1),
        ]
        self.assertEqual(queue.inorder_traversal(), expected_queue)

    def test_pop(self):
        queue = PriorityQueue()
        queue.insert("SomeTask 1", 5)
        queue.insert("SomeTask 2", 8)
        queue.insert("SomeTask 3", 3)
        queue.insert("SomeTask 4", 10)
        queue.insert("SomeTask 5", 9)
        queue.insert("SomeTask 6", 4)
        queue.insert("SomeTask 7", 1)

        popped_task = queue.pop()
        self.assertEqual(popped_task, "SomeTask 4")
        popped_task = queue.pop()
        self.assertEqual(popped_task, "SomeTask 5")

        expected_queue = [
            ("SomeTask 2", 8),
            ("SomeTask 1", 5),
            ("SomeTask 6", 4),
            ("SomeTask 3", 3),
            ("SomeTask 7", 1),
        ]
        self.assertEqual(queue.inorder_traversal(), expected_queue)

    def test_pop_empty_queue(self):
        queue = PriorityQueue()
        popped_task = queue.pop()
        self.assertIsNone(popped_task)

    def test_pop_single_task(self):
        queue = PriorityQueue()
        queue.insert("SomeTask 1", 5)
        popped_task = queue.pop()
        self.assertEqual(popped_task, "SomeTask 1")
        self.assertEqual(queue.inorder_traversal(), None)


if __name__ == "__main__":
    unittest.main()
