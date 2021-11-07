from datetime import datetime, timedelta

from homework12.base import session
from homework12.create_table import Homework, HomeworkResult, Student, Teacher


session.query(Student).delete()
session.query(Teacher).delete()
session.query(Homework).delete()
session.query(HomeworkResult).delete()

student1 = Student(name="Student_1_name", last_name="Student_1_lastname")
teacher1 = Teacher(name="Teacher_name", last_name="Teacher_lastname")
homework1 = Homework(
    text="text_example",
    teacher=teacher1,
    created=datetime.today(),
    deadline=datetime.now() + timedelta(1),
)
homework2 = teacher1.create_homework("some_text", 2)

homeworkresult2 = HomeworkResult(solution="solution_example",
                                 student=student1, homework=homework2)
homeworkresult1 = student1.do_homework(homework1, "some_text_extra")

teacher1.check_homework(homeworkresult1)
teacher1.check_homework(homeworkresult2)

session.add_all([student1, teacher1, homeworkresult1,
                 homework1, homeworkresult2])

session.commit()
