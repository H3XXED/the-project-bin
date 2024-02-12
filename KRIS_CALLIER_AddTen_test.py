import unittest
from KRIS_CALLIER_AddTen import add_10


class AdditionTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add_10(15), 25)
        self.assertEqual(add_10(2.5), 12.5)
        self.assertEqual(add_10(1 / 2), 10.5)

    def test_type(self):
        data = True
        with self.assertRaises(TypeError):
            result = add_10(data)


if __name__ == '__main__':
    unittest.main()
