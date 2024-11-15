from domain.student import Student


class Student_Service(object):
    def __init__(self, validator_student, repo_student):
        self.__valideaza_student = validator_student
        self.__student_repo = repo_student

    def add_student_to_list(self, student_id: int, nume: str, grupa: int):
        """
        Functie care valideaza si creeaza obiectul student
        input:
            student_id : int
            nume : string
            grupa : int
        """

        student = Student(student_id, nume, grupa)

        self.__valideaza_student.valideaza_student(student)

        self.__student_repo.add_student(student)

    def get_all_students(self):
        student_list = self.__student_repo.get_student_list().values()
        return [str(student) for student in student_list]

    def delete_student_from_list(self, student_id: int):
        """
        Functie care sterge un student dintr-o lista
        input:
            student_id : int
            student_list : list
        :return -
            raise ValueError cu mesajul "student inexistent"
        """
        found = True
        key_list = self.__student_repo.get_student_list()

        if student_id in key_list:
            print("okay")
        else:
            print("not okay")
