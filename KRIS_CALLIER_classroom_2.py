class Classroom:
    def __init__(self, instructor_name: str, student_grades: list[float]):
        self.instructor_name = instructor_name
        self.student_grades = student_grades

    def get_class_average(self) -> float:
        return sum(self.student_grades) / len(self.student_grades)

    def get_highest_score(self) -> float:
        return max(self.student_grades)


from typing import List


class Student:
    def __init__(self, name: str, grade: float):
        self.name = name
        self.grade = grade


class Classroom:
    def __init__(self, instructor_name: str, students: List[Student]):
        """
        Initializes a Classroom instance with an instructor name and a list of students.

        Args:
            instructor_name (str): The name of the instructor.
            students (List[Student]): A list of Student instances.
        """
        self.instructor_name = instructor_name
        self.students = students

    def get_class_average(self) -> float:
        """
        Calculates the class average grade.

        Returns:
            float: The class average grade.
        """
        grades = [student.grade for student in self.students]
        return sum(grades) / len(grades)

    def get_highest_score(self) -> float:
        """
        Finds the highest score among all students in the class.

        Returns:
            float: The highest score in the class.
        """
        grades = [student.grade for student in self.students]
        return max(grades)

    def add_student(self, name: str, grade: float):
        """
        Adds a new student to the class.

        Args:
            name (str): The name of the new student.
            grade (float): The grade of the new student.
        """
        self.students.append(Student(name, grade))

    def __str__(self):
        """
        Returns a string representation of the Classroom instance.

        Returns:
            str: A string representation of the Classroom instance.
        """
        student_info = "\n".join([f"{student.name}: {student.grade}" for student in self.students])
        return f"Instructor: {self.instructor_name}\nStudents:\n{student_info}"


if __name__ == '__main__':
    # Create an instance of the Classroom class
    classroom = Classroom("John Doe", [Student("Alice", 90), Student("Bob", 80), Student("Charlie", 85)])

    # Print the instance
    print(classroom)

    # Call the get_class_average method and display the result
    print("Class Average:", classroom.get_class_average())

    # Call the get_highest_score method and display the result
    print("Highest Score:", classroom.get_highest_score())

    # Call the add_student method
    classroom.add_student("Dave", 95)

    # Call the get_class_average method again and display the updated result
    print("Updated Class Average:", classroom.get_class_average())

