import unittest
from KRIS_CALLIER_classroom_2 import Classroom, Student


class TestClassroom(unittest.TestCase):
    """
    A unit test class for the Classroom class.
    """

    def setUp(self):
        """
        Set up a Classroom instance with some students.
        """
        self.classroom = Classroom("John Doe", [Student("Alice", 90), Student("Bob", 80), Student("Charlie", 85)])

    def test_add_student(self):
        """
        Test that adding a new student to the classroom works correctly.
        """
        self.classroom.add_student("Dave", 95)
        self.assertEqual(len(self.classroom.students), 4)
        self.assertEqual(self.classroom.students[-1].name, "Dave")
        self.assertEqual(self.classroom.students[-1].grade, 95)

    def test_get_highest_score(self):
        """
        Test that the get_highest_score method returns the correct result.
        """
        self.assertEqual(self.classroom.get_highest_score(), 90)

    def test_get_class_average(self):
        """
        Test that the get_class_average method returns the correct result.
        """
        self.assertEqual(self.classroom.get_class_average(), 85)


if __name__ == '__main__':
    unittest.main()
