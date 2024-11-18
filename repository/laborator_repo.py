from domain.problema_lab import Problema_Laborator


class LaboratorRepo(object):
    def __init__(self):
        self.__laborator_list = {}

    def get_laborators_list(self):
        return self.__laborator_list

    def add_laborator(self, laborator: Problema_Laborator):
        numar_lab = laborator.get_laborator_numar()

        if numar_lab in self.__laborator_list:
            raise ValueError("numar laborator existent \n")

        self.__laborator_list[numar_lab] = laborator

    def delete_laborator(self, lab_nr: int):
        self.__laborator_list.pop(lab_nr)

    def modify_laborator(self, laborator: Problema_Laborator):
        numar_lab = laborator.get_laborator_numar()

        if numar_lab not in self.__laborator_list:
            raise ValueError("numar laborator inexistent \n")

        self.__laborator_list[numar_lab] = laborator

    def get_lab_by_laborator_numar(self, numar_lab: int):
        if numar_lab not in self.__laborator_list:
            raise ValueError("numar laborator inexistent \n")

        return self.__laborator_list[numar_lab]
