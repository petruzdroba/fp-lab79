from domain.student import Student
from domain.problema_lab import Problema_Laborator


class Validator(object):
    def __init__(self) -> None:
        pass

    def valideaza_student(self, student: Student):
        """
        Functie care valideaza datele de intrare pentru creearea unui nou student
        input:
            student_id :int
            nume: string
            grupa : int
        :return : -
                raise ValueError with the message "id invalid", "nume invalid", "grupa invalida"
        """
        if student.get_id() < 0:
            raise ValueError("id invalid")
        if student.get_nume() == "":
            raise ValueError("nume invalid")
        if student.get_grupa() < 0:
            raise ValueError("grupa invalida")

    def valideaza_student_id(self, student_id: int, student_list: list):
        """
        Functie care verifica ca id-ul introdus de la tastatura sa fie unic
        input:
            student_id : int
            student_list : list
        :return -
            raise ValueError cu mesajul "id nu este unic"
        """
        id_list = []
        for student in student_list:
            id_list.append(student.get_id())
        pass

    def valideaza_problema(self, problema_lab: Problema_Laborator):
        """
        Fucntie care valideaza datele de intrare pt un obiect problema

        """
        if problema_lab.get_laborator_numar() < 0:
            raise ValueError("numar laborator invalid")
        if problema_lab.get_descriere() == "":
            raise ValueError("descriere invalida")
        if problema_lab.get_deadline() == "":
            raise ValueError("deadline invalid")
