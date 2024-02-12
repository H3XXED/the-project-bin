import unittest
from KRIS_CALLIER_CalcBonus import calculate_bonus


class AdditionTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculate_bonus(3, 20000), 3000.0)
        self.assertEqual(calculate_bonus(3, 9000), 675.0)
        self.assertEqual(calculate_bonus(2, 20000), 2000.0)
        self.assertEqual(calculate_bonus(2, 9000), 450.0)
        self.assertEqual(calculate_bonus(1, 20000), 1000.0)
        self.assertEqual(calculate_bonus(1, 9000), 225.0)


if __name__ == '__main__':
    unittest.main()
