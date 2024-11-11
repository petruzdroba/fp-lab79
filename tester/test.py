import domain.student


class Test(object):
    def __init__(self):
        pass

    def ruleaza_toate_testele(self):
        """
        functie care ruleaza toate testele
        :return: -
        """
        student_id = 17
        nume = "John Doe"
        grupa = 217

        student = domain.student.Student(student_id, nume, grupa)

        assert student_id == student.get_id()
        assert nume == student.get_nume()
        assert grupa == student.get_grupa()
