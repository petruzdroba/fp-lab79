from domain.validators import Validator
from domain.student import Student


class Student_Service(object):
    def __init__(self) -> None:
        pass

    def add_student_to_list(self, student_list: list, student: Student):
        """
        Functie care adauga un student intr-o lista
        input:
            student_list : list
            student: student obj
        """

        valideaza = Validator()

        valideaza.valideaza_student(student, student_list)

        student_list.append(student)

    def delete_student_from_list(self, student_list: list, student_id: int):
        """
        Functie care sterge un student dintr-o lista
        input:
            student_id : int
            student_list : list
        :return -
            raise ValueError cu mesajul "student inexistent"
        """
        for student in student_list:
            if student.get_id() == student_id:
                student_list.pop(student_list.index(student))
