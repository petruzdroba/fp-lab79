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

        valideaza.valideaza_student(student)

        student_list.append(student)
