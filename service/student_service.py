from validators.student_validator import StudentValidator
from domain.student import Student


class Student_Service(object):
    def __init__(self):
        self.__valideaza_student = StudentValidator

    def add_student_to_list(self, student_list: list, student: Student):
        """
        Functie care adauga un student intr-o lista
        input:
            student_list : list
            student: student obj
        """
        self.__valideaza_student.valideaza_student(student, student_list)

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
        found = False
        for student in student_list:
            if student.get_id() == student_id:
                student_list.pop(student_list.index(student))
                found = True
                break
        if not found:
            raise ValueError("student inexistent")
