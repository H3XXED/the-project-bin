class Classroom:
    def __init__(self, instructor_name: str, student_grades: list[float]):
        self.instructor_name = instructor_name
        self.student_grades = student_grades

    def get_class_average(self) -> float:
        return sum(self.student_grades) / len(self.student_grades)

    def get_highest_score(self) -> float:
        return max(self.student_grades)


if __name__ == '__main__':
    # Create three instances of the class Classroom with different attribute values for each instance
    classroom1 = Classroom('Mr. Hand', [90.5, 85.2, 93.7, 87.8])
    classroom2 = Classroom('John Keating', [76.2, 88.9, 92.1, 81.3])
    classroom3 = Classroom('Joe Clark', [79.3, 84.5, 87.1, 91.6])

    '''For one of the instances, print the instructor’s name, change the instructor’s name, print the updated 
    instructor’s name, and create a new attribute and display the value'''
    classroom1.instructor_name = 'Mr. Hand'
    print(classroom1.instructor_name)
    classroom1.new_attribute = 'Jaime Escalante'
    print(classroom1.new_attribute)

    # Call the get_class_average method for each class instance and display each result
    print('Class Averages:')
    print(classroom1.get_class_average())
    print('**********')
    print(classroom2.get_class_average())
    print('**********')
    print(classroom3.get_class_average())



    # Call the get_highest_score for each class instance and display each result
    print('Highest Scores:')
    print(classroom1.get_highest_score())
    print('**********')
    print(classroom2.get_highest_score())
    print('**********')
    print(classroom3.get_highest_score())
