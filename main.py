from ui.menu import Consola

from service.student_service import Student_Service
from validators.student_validator import StudentValidator
from repository.student_repo import StudentRepo
from tester.student_test import StudentTest

from validators.laborator_validator import LaboratorValidator
from repository.laborator_repo import LaboratorRepo
from service.probleme_service import Problema_Service
from tester.laborator_test import LaboratorTest

import os

StudentTest().run_all_student_test()
LaboratorTest().run_all_lab_test()

# os.system("cls")

validator_student = StudentValidator()
repo_student = StudentRepo()
service_student = Student_Service(validator_student, repo_student)

validator_laborator = LaboratorValidator()
repo_laborator = LaboratorRepo()
service_laborator = Problema_Service(validator_laborator, repo_laborator)

ui = Consola(service_student, service_laborator)

ui.run()
