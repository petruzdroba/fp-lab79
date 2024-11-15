class Consola:
    def __init__(self, student_service):
        self.__student_service = student_service
        self.__comenzi = {"add_student": self.__ui_add_student}

    def __ui_add_student(self):
        id_student = int(input("id>>>"))
        nume = input("nume>>>")
        grupa = int(input("grupa>>>"))
        self.__student_service.add_student_to_list(id_student, nume, grupa)

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
