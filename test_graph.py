import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from graph import Graph


def sample():
    g = Graph()
    g.add_road("A", "B", 1)
    g.add_road("B", "C", 1)
    g.add_road("A", "C", 5)
    g.add_road("X", "Y", 1)
    return g


class TestShortestPath(unittest.TestCase):
    def test_prefers_shorter_multi_hop(self):
        self.assertEqual(sample().shortest_path("A", "C"), (["A", "B", "C"], 2))

    def test_same_location(self):
        self.assertEqual(sample().shortest_path("A", "A"), (["A"], 0))

    def test_unreachable(self):
        path, km = sample().shortest_path("A", "X")
        self.assertIsNone(path)

    def test_unknown_location(self):
        with self.assertRaises(KeyError):
            sample().shortest_path("A", "Z")

    def test_negative_weight_rejected(self):
        with self.assertRaises(ValueError):
            Graph().add_road("A", "B", -1)


if __name__ == "__main__":
    unittest.main()
