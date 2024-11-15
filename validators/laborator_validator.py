from domain.problema_lab import Problema_Laborator


class LaboratorValidator(object):
    def __init__(self) -> None:
        pass

    def valideaza_problema(self, problema_lab: Problema_Laborator, question_list: list):
        """
        Fucntie care valideaza datele de intrare pt un obiect problema

        """
        if problema_lab.get_laborator_numar() < 0:
            raise ValueError("numar laborator invalid")
        if problema_lab.get_descriere() == "":
            raise ValueError("descriere invalida")
        if problema_lab.get_deadline() == "":
            raise ValueError("deadline invalid")

        for problema in question_list:
            if problema_lab.get_laborator_numar() == problema.get_laborator_numar():
                raise ValueError("numar laborator nu e unic")
