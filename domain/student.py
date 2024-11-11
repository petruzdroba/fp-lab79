class Student(object):
    def __init__(self, student_id: int, nume: str, grupa: int):
        self.__student_id = student_id
        self.__nume = nume
        self.__grupa = grupa

    def set_name(self, nume_nou: str):
        self.__nume = nume_nou

    def set_name(self, grupa: str):
        self.__grupa = grupa

    def get_id(self):
        return self.__student_id

    def get_nume(self):
        return self.__nume

    def get_grupa(self):
        return self.__grupa
