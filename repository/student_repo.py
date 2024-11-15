from domain.student import Student


class StudentRepo(object):
    def __init__(self):
        self.__student_list = {}

    def get_student_list(self):
        return self.__student_list

    def add_student(self, student: Student):
        id_student = student.get_id()

        if id_student in self.__student_list:
            raise ValueError("id existent \n")

        self.__student_list[id_student] = student
