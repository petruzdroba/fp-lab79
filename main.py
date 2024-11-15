from ui.menu import Consola
from service.student_service import Student_Service
from validators.student_validator import StudentValidator
from repository.student_repo import StudentRepo

import os

os.system("cls")

validator_student = StudentValidator()
repo_student = StudentRepo()

service_student = Student_Service(validator_student, repo_student)

ui = Consola(service_student)

ui.run()
