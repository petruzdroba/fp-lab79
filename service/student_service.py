from domain.student import Student


class Student_Service(object):
    def __init__(self, validator_student, repo_student):
        self.__valideaza_student = validator_student
        self.__student_repo = repo_student

    def add_student_to_list(self, student_id: int, nume: str, grupa: int):
        """
        Functie care adauga un student intr-o lista
        input:
            student_list : list
            student: student obj
        """

        student = Student(student_id, nume, grupa)

        self.__valideaza_student.valideaza_student(
            student, self.__student_repo.get_student_list()
        )

        self.__student_repo.add_student(student)

    # def delete_student_from_list(self, student_list: list, student_id: int):
    #     """
    #     Functie care sterge un student dintr-o lista
    #     input:
    #         student_id : int
    #         student_list : list
    #     :return -
    #         raise ValueError cu mesajul "student inexistent"
    #     """
    #     found = False
    #     for student in student_list:
    #         if student.get_id() == student_id:
    #             student_list.pop(student_list.index(student))
    #             found = True
    #             break
    #     if not found:
    #         raise ValueError("student inexistent")
