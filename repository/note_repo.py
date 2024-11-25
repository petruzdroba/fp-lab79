from domain.note import Note


class NoteRepo(object):
    def __init__(self):
        self.__note = {}

    def get_note_list(self):
        return self.__note

    def add_nota(self, nota: Note):
        id_nota = nota.get_id_nota()

        if id_nota in self.__note:
            raise ValueError("nota existenta")

        self.__note[id_nota] = nota
