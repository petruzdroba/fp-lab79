from domain.problema_lab import Problema_Laborator


class Problema_Service(object):
    def __init__(self, validaor_laborator, laborator_repo):
        self.__valideaza_laborator = validaor_laborator
        self.__laborator_repo = laborator_repo

    def add_problem_to_list(self, numar_laborator: int, descriere: str, deadline: str):
        """
        Functie care adauga o problema la lista de probleme
        import :
            list_of_questions : list of obj
            problem : obj
        :returns : -
        """

        laborator = Problema_Laborator(numar_laborator, descriere, deadline)

        self.__valideaza_laborator.valideaza_laborator(laborator)

        self.__laborator_repo.add_laborator(laborator)

    def get_all_laborators(self):
        lab_list = self.__laborator_repo.get_laborators_list().values()
        return [str(labs) for labs in lab_list]

    # def delete_problem_from_list(self, list_of_questions: list, numar_laborator: int):
    #     """
    #     Functie care sterge problema cu numarul de laborator numar_laborator din lista
    #     input:
    #         numar_laborator : int
    #         list_of_questions : lsit
    #     :return -
    #         raise Value Error cu mesajul "problema inexistenta"
    #     """
    #     found = False

    #     for question in list_of_questions:
    #         if question.get_laborator_numar() == numar_laborator:
    #             list_of_questions.pop(list_of_questions.index(question))
    #             found = True
    #             break

    #     if not found:
    #         raise ValueError("problema inexistenta")
