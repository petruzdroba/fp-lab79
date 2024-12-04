from domain.student import Student
from service.student_service import Student_Service
from validators.student_validator import StudentValidator
from repository.student_repo import StudentRepo
import random


class StudentTest(object):
    def __init__(self):
        self.__test_validator = StudentValidator()
        self.__test_repo = StudentRepo("test_students.txt")
        self.__test_service = Student_Service(self.__test_validator, self.__test_repo)

    def run_all_student_test(self):
        self.__reset_test_repo()
        self.__test_read_student_from_file()
        self.__test_create_student()
        self.__test_add()

        self.__test_search()

        self.__test_delete()

        self.__test_random_generator()

    def __test_read_student_from_file(self):
        print(self.__test_repo.get_student_list())
        assert len(self.__test_repo.get_student_list()) == 0

    def __reset_test_repo(self):
        self.__test_repo.get_student_list().clear()

        with open("test_students.txt", "w") as file:
            file.write("")

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

    def __test_add(self):
        test_id = 13
        test_nume = "John Doe"
        test_grupa = 217
        self.__test_service.add_student_to_list(test_id, test_nume, test_grupa)
        assert test_id in self.__test_repo.get_student_list()

    def __test_delete(self):
        # deletes student added in previous test function
        test_id = 13

        self.__test_service.delete_student_from_list(test_id)

        assert test_id not in self.__test_repo.get_student_list()

    def __test_search(self):
        test_id = 13
        test_nume = "John Doe"
        test_grupa = 217

        test_student = self.__test_service.search_student_from_list(test_id)

        assert (
            test_student.get_id() == test_id
            and test_student.get_nume() == test_nume
            and test_student.get_grupa() == test_grupa
        )

    def __test_random_generator(self):
        random.seed(69)

        self.__test_service.generate_nr_students_random(1)

        test_student = self.__test_service.search_student_from_list(703)

        assert (
            test_student.get_nume() == "Dat Kueaeaox"
            and test_student.get_id() == 703
            and test_student.get_grupa() == 74
        )
