import pytest

import homework6.task02 as task2
from homework6.task02 import Student, Teacher

teacher_1 = Teacher("Viktor", "Vasiliev")
teacher_2 = Teacher("Andrey", "Andreev")

student_1 = Student("Sergey", "Vasin")
student_2 = Student("Alex", "Petrov")

oop_hw = teacher_1.create_homework("Learn OOP", 1)
other_hw = teacher_1.create_homework("Some hw", 5)

result_1 = student_2.do_homework(oop_hw, "I have done this hw")
result_2 = student_2.do_homework(other_hw, "I have done this hw too")
result_3 = student_1.do_homework(other_hw, "done")


def test_check_same_result():
    teacher_1.check_homework(result_1)
    temp_1 = teacher_1.homework_done

    teacher_2.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2

    teacher_1.check_homework(result_2)
    teacher_1.check_homework(result_3)


@pytest.mark.xfail(raises=task2.NotHomework)
def test_not_homework_exception():
    task2.HomeworkResult(student_2, "wow", "wowowow")


@pytest.mark.xfail(raises=task2.DeadlineError)
def test_deadline_exception():
    test = teacher_1.create_homework("test", -1)
    student_1.do_homework(test, "test")


def test_reset_results():
    test_hw = Teacher.create_homework("hw", 1)
    res = student_2.do_homework(test_hw, "test>5")
    Teacher.check_homework(res)

    assert test_hw in Teacher.homework_done
    assert res in teacher_2.homework_done[test_hw]
    Teacher.reset_results(test_hw)

    assert test_hw not in teacher_1.homework_done
    assert res not in Teacher.homework_done[test_hw]

    Teacher.reset_results()

    assert Teacher.homework_done is not True


def test_check_homework_no_duplicates():
    test_hw = Teacher.create_homework("hw", 1)
    res = student_2.do_homework(test_hw, "test>5")
    Teacher.check_homework(res)
    Teacher.check_homework(res)
    Teacher.check_homework(res)

    assert len(Teacher.homework_done[test_hw]) == 1
