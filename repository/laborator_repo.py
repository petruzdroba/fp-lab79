from domain.problema_lab import Problema_Laborator


class LaboratorRepo(object):
    def __init__(self, file_path):
        self.__laborator_list = {}
        self.__file_path = file_path
        self.__citire_din_fisier()

    def __citire_din_fisier(self):
        with open(self.__file_path, "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line != "":
                    parti = line.split(",")
                    laborator = Problema_Laborator(int(parti[0]), parti[1], parti[2])
                    self.__laborator_list[int(parti[0])] = laborator

    def __adauga_laborator_in_fisier(self, laborator: Problema_Laborator):
        with open(self.__file_path, "a") as f:
            f.write(
                f"{laborator.get_laborator_numar()},{laborator.get_descriere()},{laborator.get_deadline()}\n"
            )

    def __overwrite_laborator_in_fisier(self):
        with open(self.__file_path, "w") as f:
            for laborator in self.__laborator_list.values():
                f.write(
                    f"{laborator.get_laborator_numar()},{laborator.get_descriere()},{laborator.get_deadline()}\n"
                )

    def get_laborators_list(self):
        return self.__laborator_list

    def add_laborator(self, laborator: Problema_Laborator):
        numar_lab = laborator.get_laborator_numar()

        if numar_lab in self.__laborator_list:
            raise ValueError("numar laborator existent \n")

        self.__laborator_list[numar_lab] = laborator
        self.__adauga_laborator_in_fisier(laborator)

    def delete_laborator(self, lab_nr: int):
        self.__laborator_list.pop(lab_nr)
        self.__overwrite_laborator_in_fisier()

    def modify_laborator(self, laborator: Problema_Laborator):
        numar_lab = laborator.get_laborator_numar()

        if numar_lab not in self.__laborator_list:
            raise ValueError("numar laborator inexistent \n")

        self.__laborator_list[numar_lab] = laborator
        self.__overwrite_laborator_in_fisier()

    def get_lab_by_laborator_numar(self, numar_lab: int):
        if numar_lab not in self.__laborator_list:
            raise ValueError("numar laborator inexistent \n")

        return self.__laborator_list[numar_lab]
