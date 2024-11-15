from domain.problema_lab import Problema_Laborator
from validators.laborator_validator import LaboratorValidator


class Problema_Service(object):
    def __init__(self) -> None:
        self.__valideaza_laborator = LaboratorValidator

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
        self.__valideaza_laborator.valideaza_problema(problema, list_of_questions)

        list_of_questions.append(problema)

    def delete_problem_from_list(self, list_of_questions: list, numar_laborator: int):
        """
        Functie care sterge problema cu numarul de laborator numar_laborator din lista
        input:
            numar_laborator : int
            list_of_questions : lsit
        :return -
            raise Value Error cu mesajul "problema inexistenta"
        """
        found = False

        for question in list_of_questions:
            if question.get_laborator_numar() == numar_laborator:
                list_of_questions.pop(list_of_questions.index(question))
                found = True
                break

        if not found:
            raise ValueError("problema inexistenta")
