from domain.student import Student


class StudentValidator(object):
    def __init__(self) -> None:
        pass

    def valideaza_student(self, student: Student):
        """
        Functie care valideaza datele de intrare pentru creearea unui nou student
        input:
            student : Student
            student_list : list
        :return : -
                raise ValueError with the message "id invalid", "nume invalid", "grupa invalida"
        """
        if student.get_id() < 0:
            raise ValueError("id invalid")

        nume = student.get_nume().strip()
        if nume == "":
            erori += "nume invalid!\n"
        elif not nume.isalpha():
            erori += "numele trebuie să conțină doar litere!\n"
        elif not nume.istitle():
            erori += "nume trebuie să înceapă cu literă mare!\n"

        if student.get_grupa() < 0:
            raise ValueError("grupa invalida")
