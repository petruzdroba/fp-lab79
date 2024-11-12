from domain.problema_lab import Problema_Laborator
from domain.validators import Validator


class Problema_Service(object):
    def __init__(self) -> None:
        pass

    def add_problem_to_list(
        self, list_of_questions: list, problema: Problema_Laborator
    ):
        """
        Functie care adauga o problema la lista de probleme
        import :
            list_of_questions : list of obj
            problem : obj
        :returns : -
        """
        valideaza = Validator()

        valideaza.valideaza_problema(problema, list_of_questions)

        list_of_questions.append(problema)
