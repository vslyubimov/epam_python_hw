import unittest

from homework5.task01 import Homework, Student, Teacher


class TestTask01Classes(unittest.TestCase):

    def setUp(self):
        self.homework = Homework
        self.student = Student
        self.teacher = Teacher

    def test_class_homework_method_is_active(self):
        self.assertEqual(self.homework('task', 5).is_active(), True)

    def test_class_student_method_is_active_throw_do_homework(self):
        self.assertEqual(self.student('Roman', 'Petrov')
                         .do_homework(Homework(Homework, 5))
                         .is_active(), Homework(Homework, 5).is_active())

    def test_class_student_method_is_active_throw_do_homework_negative(self):
        self.assertEqual(self.student('Roman', 'Petrov')
                         .do_homework(Homework(Homework, 0)), None)

    def test_class_teacher_method_create_homework_check_deadline(self):
        self.assert_(self.teacher('Daniil', 'Romanov')
                     .create_homework(Homework, 5)
                     .deadline, Homework(Homework, 5).deadline)


if __name__ == "__main__":
    unittest.main()

    # student = Student('Roman', 'Petrov')
    #
    # teacher.last_name == 'Daniil'  # Daniil
    # student.first_name == 'Petrov'  # Petrov
    #
    # expired_homework = teacher.create_homework('Learn functions', 0)
    # expired_homework.created  # Example: 2019-05-26 16:44:30.688762
    # expired_homework.deadline  # 0:00:00
    # expired_homework.text  # 'Learn functions'
    #
    # # create function from method and use it
    # create_homework_too = teacher.create_homework
    # oop_homework = create_homework_too('create 2 simple classes', 5)
    # oop_homework.deadline  # 5 days, 0:00:00
    #
    # student.do_homework(oop_homework)
    # student.do_homework(expired_homework)  # You are late
