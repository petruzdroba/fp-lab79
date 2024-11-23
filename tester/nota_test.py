from domain.note import Note
from domain.student import Student
from domain.problema_lab import Problema_Laborator


class NotaTest(object):
    def __init__(self):
        pass

    def run_all_nota_test(self):
        self.__test_create_nota()

    def __test_create_nota(self):
        test_id = 13
        test_nume = "John Doe"
        test_grupa = 217

        test_student = Student(test_id, test_nume, test_grupa)

        test_lab_nr = 13
        test_descriere = "Test"
        test_deadline = "12.12.2012"

        test_lab = Problema_Laborator(test_lab_nr, test_descriere, test_deadline)

        test_id_nota = 13
        test_nota = 5

        test_note = Note(test_id_nota, test_student, test_lab, test_nota)

        assert test_note.get_student() == test_student
        assert test_note.get_laborator() == test_lab
        assert test_note.get_id_nota() == test_id_nota
        assert test_note.get_nota() == test_nota
