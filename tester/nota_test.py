from domain.note import Note
from domain.student import Student
from domain.problema_lab import Problema_Laborator

from repository.note_repo import NoteRepo
from repository.student_repo import StudentRepo
from repository.laborator_repo import LaboratorRepo

from validators.note_validator import NoteValidator

from service.note_service import NoteService


class NotaTest(object):
    def __init__(self):
        self.__test_student_repo = StudentRepo()
        self.__test_lab_repo = LaboratorRepo()
        self.__test_note_repo = NoteRepo()
        self.__test_note_validator = NoteValidator()
        self.__test_service = NoteService(
            self.__test_note_validator,
            self.__test_note_repo,
            self.__test_student_repo,
            self.__test_lab_repo,
        )

    def run_all_nota_test(self):
        self.__test_create_nota()
        self.__test_add_nota()

    def __test_create_nota(self):
        test_id = 13
        test_nume = "John Doe"
        test_grupa = 217

        test_student = Student(test_id, test_nume, test_grupa)
        self.__test_student_repo.add_student(test_student)

        test_lab_nr = 13
        test_descriere = "Test"
        test_deadline = "12.12.2012"

        test_lab = Problema_Laborator(test_lab_nr, test_descriere, test_deadline)
        self.__test_lab_repo.add_laborator(test_lab)

        test_id_nota = 13
        test_nota = 5

        test_note = Note(test_id_nota, test_student, test_lab, test_nota)

        assert test_note.get_student() == test_student
        assert test_note.get_laborator() == test_lab
        assert test_note.get_id_nota() == test_id_nota
        assert test_note.get_nota() == test_nota

    def __test_add_nota(self):
        test_id_student = 13
        test_lab_nr = 13
        test_id_nota = 13
        test_nota = 5

        self.__test_service.add_nota_to_list(
            test_id_nota, test_id_student, test_lab_nr, test_nota
        )

        assert test_id_nota in self.__test_note_repo.get_note_list()
