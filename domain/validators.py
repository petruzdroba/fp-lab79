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