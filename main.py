from tester.test import Test
from ui.menu import meniu_consola

import os

teste = Test()

os.system("cls")
teste.ruleaza_toate_testele()

student_list = []
question_list = []

meniu_consola(student_list, question_list)
