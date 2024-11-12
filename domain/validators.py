from domain.student import Student
from domain.problema_lab import Problema_Laborator


class Validator(object):
    def __init__(self) -> None:
        pass

    def valideaza_student(self, student: Student, student_list: list):
        """
        Functie care valideaza datele de intrare pentru creearea unui nou student
        input:
            student : Student
            student_list : list
        :return : -
                raise ValueError with the message "id invalid", "nume invalid", "grupa invalida"
        """
        if student.get_id() < 0:
            raise ValueError("id invalid")
        if student.get_nume() == "":
            raise ValueError("nume invalid")
        if student.get_grupa() < 0:
            raise ValueError("grupa invalida")

        for elev in student_list:
            if student.get_id() == elev.get_id():
                raise ValueError("id nu e unic")

    def valideaza_problema(self, problema_lab: Problema_Laborator, question_list: list):
        """
        Fucntie care valideaza datele de intrare pt un obiect problema

        """
        if problema_lab.get_laborator_numar() < 0:
            raise ValueError("numar laborator invalid")
        if problema_lab.get_descriere() == "":
            raise ValueError("descriere invalida")
        if problema_lab.get_deadline() == "":
            raise ValueError("deadline invalid")

        for problema in question_list:
            if problema_lab.get_laborator_numar() == problema.get_laborator_numar():
                raise ValueError("numar laborator nu e unic")
