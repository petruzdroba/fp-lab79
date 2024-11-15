from domain.student import Student


class StudentTest(object):
    def __init__(self):
        self.__test_student_repo = {}

    def run_all_student_test(self):
        self.__test_create_student()

    def __test_create_student(self):
        test_id = 13
        test_nume = "John Doe"
        test_grupa = 217

        test_student = Student(test_id, test_nume, test_grupa)

        assert (
            test_student.get_id() == test_id
            and test_student.get_nume() == test_nume
            and test_student.get_grupa() == test_grupa
        )
