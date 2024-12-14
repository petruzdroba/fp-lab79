from domain.problema_lab import Problema_Laborator
from validators.laborator_validator import LaboratorValidator
from repository.laborator_repo import LaboratorRepo
from service.probleme_service import Problema_Service


class LaboratorTest(object):
    def __init__(self):
        self.__test_validator = LaboratorValidator()
        self.__test_repo = LaboratorRepo("test_laborator.txt")
        self.__test_service = Problema_Service(self.__test_validator, self.__test_repo)

    def run_all_lab_test(self):
        self.__reset_test_repo()
        self.__test_read_from_file()
        self.__test_create_lab()
        self.__test_add()
        self.__test_search()

        self.__test_delete()

    def __test_read_from_file(self):
        assert len(self.__test_repo.get_laborators_list()) == 0

    def __reset_test_repo(self):
        self.__test_repo.get_laborators_list().clear()
        with open("test_laborators.txt", "w") as file:
            file.write("")

    def __test_create_lab(self):
        test_lab_nr = 13
        test_descriere = "Test"
        test_deadline = "12.12.2012"

        test_lab = Problema_Laborator(test_lab_nr, test_descriere, test_deadline)

        assert (
            test_lab.get_laborator_numar() == test_lab_nr
            and test_lab.get_descriere() == test_descriere
            and test_lab.get_deadline() == test_deadline
        )

    def __test_add(self):
        test_lab_nr = 13
        test_descriere = "Test"
        test_deadline = "12.12.2012"

        self.__test_service.add_problem_to_list(
            test_lab_nr, test_descriere, test_deadline
        )

        assert test_lab_nr in self.__test_repo.get_laborators_list()

    def __test_delete(self):
        test_lab_nr = 13

        self.__test_service.delete_problem_from_list(test_lab_nr)

        assert test_lab_nr not in self.__test_repo.get_laborators_list()

    def __test_search(self):
        test_lab_nr = 13
        test_descriere = "Test"
        test_deadline = "12.12.2012"

        test_lab = self.__test_service.search_laborator_from_list(test_lab_nr)

        assert (
            test_lab.get_laborator_numar() == test_lab_nr
            and test_lab.get_descriere() == test_descriere
            and test_lab.get_deadline() == test_deadline
        )
