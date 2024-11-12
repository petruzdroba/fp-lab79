from service.student_service import Student_Service
from service.probleme_service import Problema_Service

from domain.student import Student
from domain.problema_lab import Problema_Laborator


def meniu_consola(student_list: list, question_list: list):
    print("1. Studenti")
    print("2. Probleme")
    print("3. Exit")
    choice = int(input(">>>"))

    if choice == 1:
        meniu_studenti(student_list)
        meniu_consola(student_list, question_list)
    elif choice == 2:
        meniu_probleme_laborator(question_list)
        meniu_consola(student_list, question_list)
    else:
        return 0


def meniu_studenti(student_list: list):
    print("1. Adauga student")
    print("2. Sterge student")
    choice = int(input(">>>"))

    if choice == 1:
        student_id = int(input("id>>>"))
        nume = input("nume>>>")
        grupa = int(input("grupa>>>"))

        student = Student(student_id, nume, grupa)

        Student_Service().add_student_to_list(student_list, student)
        meniu_studenti(student_list)
    elif choice == 2:
        student_id = int(input("id>>>"))

        Student_Service().delete_student_from_list(student_list, student_id)

        meniu_studenti(student_list)


def meniu_probleme_laborator(question_list: list):
    print("1. Adauga problema laborator")
    print("2. Sterge problema laborator")
    choice = int(input(">>>"))
    if choice == 1:
        numar_lab = int(input("numar_laborator>>>"))
        descriere = input("descriere>>>")
        deadline = input("deadline>>>")

        problema = Problema_Laborator(numar_lab, descriere, deadline)

        Problema_Service().add_problem_to_list(question_list, problema)
        meniu_probleme_laborator(question_list)
    elif choice == 2:
        numar_lab = int(input("numar_laborator>>>"))
        Problema_Service.delete_problem_from_list(question_list, numar_lab)

        meniu_probleme_laborator(question_list)
