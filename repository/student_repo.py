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

    def delete_student(self, student_id: int):
        self.__student_list.pop(student_id)

    def modify_student(self, student: Student):
        id_student = student.get_id()

        if id_student not in self.__student_list:
            raise ValueError("id inexistent \n")

        self.__student_list[id_student] = student

    def get_student_by_id(self, id_student: int):
        if id_student not in self.__student_list:
            raise ValueError("id inexistent \n")

        return self.__student_list[id_student]
