import unittest
from KRIS_CALLIER_Plant import Plant


class TestPlant(unittest.TestCase):
    def test_grow(self):
        # create a plant with initial height 5.0 inches
        p = Plant("Rose", 5.0)
        # grow it slowly
        p.grow("slow")
        # the new height should be 6.0 inches
        self.assertEqual(p.height, 6.0)
        # grow it fast
        p.grow("fast")
        # the new height should be 8.0 inches
        self.assertEqual(p.height, 8.0)


if __name__ == '__main__':
    unittest.main()
