class Validator(object):
    def __init__(self) -> None:
        pass

    def valideaza_student(self, student_id: int, nume: str, grupa: int):
        """
        Functie care valideaza datele de intrare pentru creearea unui nou student
        input:
            student_id :int
            nume: string
            grupa : int
        :return : -
                raise ValueError with the message "id invalid", "nume invalid", "grupa invalida"
        """
        if student_id < 0:
            raise ValueError("id invalid")
        if nume == "":
            raise ValueError("nume invalid")
        if grupa < 0:
            raise ValueError("grupa invalida")

    def valideaza_problema(self, laborator_numar: int, descirere: str, deadline: str):
        """
        Fucntie care valideaza datele de intrare pt un obiect problema

        """
        if laborator_numar < 0:
            raise ValueError("numar laborator invalid")
        if descirere == "":
            raise ValueError("descriere invalida")
        if deadline == "":
            raise ValueError("deadl;ine invalid")
