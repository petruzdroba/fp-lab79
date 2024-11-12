from tester.test import Test
from ui.menu import meniu_consola

import os

teste = Test()

teste.ruleaza_toate_testele()

student_list = []
question_list = []

os.system("cls")
meniu_consola(student_list, question_list)
