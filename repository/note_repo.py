class NoteRepo(object):
    def __init__(self):
        self.__note = {}

    def get_note_list(self):
        return self.__note
