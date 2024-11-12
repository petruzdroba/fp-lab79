import domain.student
from domain.problema_lab import Problema_Laborator

from service.student_service import Student_Service
from service.probleme_service import Problema_Service


class Test(object):
    test_student_list = []
    test_problem_list = []

    def __init__(self):
        pass

    def ruleaza_toate_testele(self):
        """
        functie care ruleaza toate testele
        :return: -
        """
        self.test_creeaza_student()
        self.test_creeaza_problema()
        self.test_adauga_student_lista(self.test_student_list)
        self.test_adauga_problema_lista(self.test_problem_list)

        self.test_sterge_student_din_lista(self.test_student_list)

    def test_creeaza_student(self):
        student_id = 17
        nume = "John Doe"
        grupa = 217

        student = domain.student.Student(student_id, nume, grupa)

        assert student_id == student.get_id()
        assert nume == student.get_nume()
        assert grupa == student.get_grupa()

    def test_creeaza_problema(self):
        laborator_numar = 7
        descriere = "o problema foarte frumoasa"
        deadline = "11/11/2024"

        problema_test = Problema_Laborator(laborator_numar, descriere, deadline)

        assert laborator_numar == problema_test.get_laborator_numar()
        assert descriere == problema_test.get_descriere()
        assert deadline == problema_test.get_deadline()

    def test_adauga_student_lista(self, test_student_list: list):
        student_id = 17
        nume = "John Doe"
        grupa = 217

        student = domain.student.Student(student_id, nume, grupa)

        service = Student_Service()

        service.add_student_to_list(test_student_list, student)

        assert test_student_list[0] == student

        print("Tests passed succesfully")

    def test_adauga_problema_lista(self, test_problem_list: list):
        laborator_numar = 7
        descriere = "o problema foarte frumoasa"
        deadline = "11/11/2024"

        problema_test = Problema_Laborator(laborator_numar, descriere, deadline)

        service = Problema_Service()

        service.add_problem_to_list(test_problem_list, problema_test)

        assert test_problem_list[0] == problema_test

    def test_sterge_student_din_lista(self, test_student_list: list):
        student_id = 17

        service = Student_Service()

        service.delete_student_from_list(test_student_list, student_id)

        assert len(test_student_list) == 0
