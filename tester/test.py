import domain.student
from service.student_service import Student_Service


class Test(object):
    test_student_list = []

    def __init__(self):
        pass

    def ruleaza_toate_testele(self):
        """
        functie care ruleaza toate testele
        :return: -
        """
        self.test_creeaza_student()
        self.test_adauga_student_lista(self.test_student_list)

    def test_creeaza_student(self):
        student_id = 17
        nume = "John Doe"
        grupa = 217

        student = domain.student.Student(student_id, nume, grupa)

        assert student_id == student.get_id()
        assert nume == student.get_nume()
        assert grupa == student.get_grupa()

    def test_adauga_student_lista(self, test_student_list: list):
        student_id = 17
        nume = "John Doe"
        grupa = 217

        student = domain.student.Student(student_id, nume, grupa)

        service = Student_Service()

        service.add_student_to_list(test_student_list, student)

        assert test_student_list[0] == student

        print("Tests passed succesfully")
