import unittest
from KRIS_CALLIER_Classroom import Classroom


class TestClassroom(unittest.TestCase):
    def setUp(self):
        self.classroom1 = Classroom('Teacher', [90.5, 85.2, 93.7, 87.8])
        self.classroom2 = Classroom('Instructor', [76.2, 88.9, 92.1, 81.3])
        self.classroom3 = Classroom('Educator', [79.3, 84.5, 87.1, 91.6])

    def test_get_class_average(self):
        self.assertAlmostEqual(self.classroom1.get_class_average(), 89.3, places=1)
        self.assertAlmostEqual(self.classroom2.get_class_average(), 84.6, places=1)
        self.assertAlmostEqual(self.classroom3.get_class_average(), 85.6, places=1)

    def test_get_highest_score(self):
        self.assertAlmostEqual(self.classroom1.get_highest_score(), 93.7, places=1)
        self.assertAlmostEqual(self.classroom2.get_highest_score(), 92.1, places=1)
        self.assertAlmostEqual(self.classroom3.get_highest_score(), 91.6, places=1)


if __name__ == '__main__':
    unittest.main()
