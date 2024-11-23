from domain.note import Note
from validators.note_validator import NoteValidator


from repository.note_repo import NoteRepo
from repository.student_repo import StudentRepo
from repository.laborator_repo import LaboratorRepo


class NoteService(object):
    def __init__(
        self,
        validator_note: NoteValidator,
        repo_note,
        repo_student: StudentRepo,
        repo_laborator: LaboratorRepo,
    ):
        self.__validator_note = validator_note
        self.__repo_note = repo_note
        self.__student_repo = repo_student
        self.__laborator_repo = repo_laborator

    def add_nota_to_list(
        self, id_nota: int, id_student: int, id_laborator: int, nota: int
    ):
        """
        Functie care adauga nota nota
        """
        student = self.__student_repo.get_student_by_id(id_student)
        laborator = self.__laborator_repo.get_lab_by_laborator_numar(id_laborator)

        nota_noua = Note(id_nota, student, laborator, nota)

        self.__validator_note.valideaza_nota(nota_noua)

        self.__repo_note.add_nota(nota_noua)
