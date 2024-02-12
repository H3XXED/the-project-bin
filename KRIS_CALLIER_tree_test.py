import unittest
from KRIS_CALLIER_tree import Tree


class TestTree(unittest.TestCase):
    def setUp(self):
        self.tree = Tree("Oak", 60.0, 1000)

    def test_grow_slow(self):
        """Test that the tree grows at a slow rate."""
        self.tree.grow("slow")
        self.assertEqual(self.tree.height, 70.0)

    def test_grow_fast(self):
        """Test that the tree grows at a fast rate."""
        self.tree.grow("fast")
        self.assertEqual(self.tree.height, 80.0)

    def test_fall(self):
        """Test that the tree loses all of its leaves."""
        self.tree.fall()
        self.assertEqual(self.tree.num_leaves, 0)


if __name__ == '__main__':
    unittest.main()

