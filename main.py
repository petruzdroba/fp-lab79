from ui.menu import Consola

from service.student_service import Student_Service
from validators.student_validator import StudentValidator
from repository.student_repo import StudentRepo
from tester.student_test import StudentTest

from validators.laborator_validator import LaboratorValidator
from repository.laborator_repo import LaboratorRepo
from service.probleme_service import Problema_Service
from tester.laborator_test import LaboratorTest

from tester.nota_test import NotaTest

import random
import os

StudentTest().run_all_student_test()
LaboratorTest().run_all_lab_test()
NotaTest().run_all_nota_test()

# os.system("cls")

validator_student = StudentValidator()
repo_student = StudentRepo()
service_student = Student_Service(validator_student, repo_student)
service_student.generate_nr_students_random(random.randint(10, 21))

validator_laborator = LaboratorValidator()
repo_laborator = LaboratorRepo()
service_laborator = Problema_Service(validator_laborator, repo_laborator)

ui = Consola(service_student, service_laborator)

ui.run()
