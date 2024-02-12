class Student:
    def __init__(self, name, grade):
        """
        Constructor of Student class.

        Args:
            name (str): The student's name.
            grade (float): The student's grade.

        Returns:
            None.
        """
        self.name = name
        self.grade = grade

    def __str__(self):
        """
        Create a string with all of the attributes of the Student class.

        Args:
            None.

        Returns:
            str: A string with the student's name and grade.
        """
        return f"Name: {self.name}, Grade: {self.grade}"


# Create two instances of the Student class
student1 = Student("Kris Callier", 4.0)
student2 = Student("Mary Lamb", 3.5)

# Print the instances
print(student1)
print(student2)
