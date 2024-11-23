from domain.note import Note
from validators.note_validator import NoteValidator


from repository.note_repo import NoteRepo
from repository.student_repo import StudentRepo
from repository.laborator_repo import LaboratorRepo


class NoteService(object):
    def __init__(
        self,
        validator_note: NoteValidator,
        repo_note: NoteRepo,
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

    def get_all_notes(self):
        note_list = self.__repo_note.get_note_list().values()
        return [str(note) for note in note_list]

    def __grades_by_lab(self, id_lab: int):
        note_list = self.__repo_note.get_note_list().values()

        note_filtered = {}

        for nota in note_list:
            if nota.get_laborator().get_laborator_numar() == id_lab:
                note_filtered[nota.get_id_nota()] = nota

        return note_filtered

    def __filter_alpha(self, dicts):
        sorted_dict = dict(
            sorted(dicts.items(), key=lambda item: item[1].get_student().get_nume())
        )
        return sorted_dict

    def get_notes_by_lab_alpha(self, id_laborator: int):
        """
        Functie care returneaza o lista de note la un laborator dat : id_laborator si o sorteaza
        alfabetic dupa numele studentilor
        """
        if id_laborator not in self.__laborator_repo.get_laborators_list():
            raise ValueError("id laborator inexistent")

        note_filtered = self.__grades_by_lab(id_laborator)

        note_filtered = self.__filter_alpha(note_filtered).values()
        return [str(note) for note in note_filtered]

    def __filter_grade(self, dicts):
        sorted_dict = dict(
            sorted(dicts.items(), key=lambda item: item[1].get_nota(), reverse=True)
        )
        return sorted_dict

    def get_notes_by_lab_grade(self, id_laborator: int):
        if id_laborator not in self.__laborator_repo.get_laborators_list():
            raise ValueError("id laborator inexistent")

        note_filtered = self.__grades_by_lab(id_laborator)
        note_filtered = self.__filter_grade(note_filtered).values()

        return [str(note) for note in note_filtered]
