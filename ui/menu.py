class Consola:
    def __init__(self, student_service, laborator_service):
        self.__student_service = student_service
        self.__laborator_service = laborator_service
        self.__comenzi = {
            "add_student": self.__ui_add_student,
            "add_laborator": self.__ui_add_laborator,
            "show_students": self.__ui_show_studenti,
            "show_laborators": self.__ui_show_laborators,
        }

    def __ui_add_student(self):
        id_student = int(input("id>>>"))
        nume = input("nume>>>")
        grupa = int(input("grupa>>>"))
        self.__student_service.add_student_to_list(id_student, nume, grupa)

    def __ui_add_laborator(self):
        numar_lab = int(input("nrlab>>>"))
        descriere = input("descriere>>>")
        deadline = input("deadline>>>")

        self.__laborator_service.add_problem_to_list(numar_lab, descriere, deadline)

    def __ui_show_studenti(self):
        studenti = self.__student_service.get_all_students()
        for student in studenti:
            print(student)

    def __ui_show_laborators(self):
        labs = self.__laborator_service.get_all_laborators()
        for lab in labs:
            print(lab)

    def run(self):
        while True:
            nume_comanda = input(">>>")
            nume_comanda = nume_comanda.lower().strip()
            if nume_comanda == "":
                continue

            if nume_comanda == "exit":
                break

            if nume_comanda in self.__comenzi:
                try:
                    self.__comenzi[nume_comanda]()
                except ValueError:
                    print("valoare numerica invalida!\n")
            else:
                print("comanda invalida!\n")
