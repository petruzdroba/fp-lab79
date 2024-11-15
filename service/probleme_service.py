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

    def delete_problem_from_list(self, laborator_number: int):
        """
        Functie care sterge problema cu numarul de laborator numar_laborator din lista
        input:
            numar_laborator : int
        :return -
            raise Value Error cu mesajul "laborator inexistenta"
        """
        if laborator_number in self.__laborator_repo.get_laborators_list():
            self.__laborator_repo.delete_laborator(laborator_number)
        else:
            raise ValueError("laborator inexistent")
