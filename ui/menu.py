from service.student_service import Student_Service
from domain.student import Student


def meniu_consola(student_list: list):
    print("1. Adauga student")
    choice = int(input(">>>"))

    if choice == 1:
        student_id = int(input("id>>>"))
        nume = input("nume>>>")
        grupa = int(input("grupa>>>"))

        student = Student(student_id, nume, grupa)

        service = Student_Service()

        service.add_student_to_list(student_list, student)
