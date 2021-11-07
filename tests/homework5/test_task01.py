import datetime

import pytest

from homework5.task01 import Homework, Student, Teacher


@pytest.mark.parametrize(("name", "last_name"), [("Sergey", "Petrov")])
def test_teacher_name_lastname(name, last_name):
    teacher = Teacher(last_name, name)

    assert teacher.last_name == last_name
    assert teacher.first_name == name


@pytest.mark.parametrize(("name", "last_name"), [("Petr", "Sergeev")])
def test_student_name_lastname(name, last_name):
    student = Teacher(last_name, name)

    assert student.last_name == last_name
    assert student.first_name == name


def test_homework():
    none_work = Homework("test", 0)
    done_work = Homework("test", 2)
    none_work.created = datetime.datetime.today() - datetime.timedelta(1)
    done_work.created = datetime.datetime.today() - datetime.timedelta(1)

    assert Student.do_homework(none_work) is None
    assert Student.do_homework(done_work) == done_work
