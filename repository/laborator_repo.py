from domain.problema_lab import Problema_Laborator


class LaboratorRepo(object):
    def __init__(self):
        self.__laborator_list = {}

    def get_laborators_list(self):
        return self.__laborator_list

    def add_laborator(self, laborator: Problema_Laborator):
        numar_lab = laborator.get_laborator_numar()

        self.__laborator_list[numar_lab] = laborator
