"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную
1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)
HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'
    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания
2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.
3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования
4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.
    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.
PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""

import datetime
from collections import defaultdict


class NotHomework(Exception):
    def __init__(self, message="You gave not a homework object"):
        self.message = message
        super().__init__(self.message)


class DeadlineError(Exception):
    def __init__(self, message="You are late"):
        self.message = message
        super().__init__(self.message)


class Person:
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name


class Homework:
    def __init__(self, text, deadline):
        self.text = text
        self.created = datetime.datetime.today()
        self.deadline = datetime.timedelta(deadline)

    def is_active(self):
        return datetime.datetime.today() <= self.deadline + self.created


class Student(Person):

    def do_homework(self, todo, solution):
        if todo.is_active():
            return HomeworkResult(self, todo, solution)
        raise DeadlineError


class HomeworkResult:

    def __init__(self, author, hw_name, solution):
        self.author = author
        self.solution = solution
        if not isinstance(hw_name, Homework):
            raise NotHomework
        self.hw_name = hw_name


class Teacher(Person):
    homework_done = defaultdict(list)

    @staticmethod
    def create_homework(text, deadline):
        return Homework(text, deadline)

    @classmethod
    def check_homework(cls, checking):
        flag_sol_true = len(checking.solution) >= 5
        if flag_sol_true and checking \
                not in cls.homework_done[checking.hw_name]:
            cls.homework_done[checking.hw_name].append(checking)
        return flag_sol_true

    @classmethod
    def reset_results(cls, hw=None):
        if hw is None:
            cls.homework_done.clear()
        else:
            del cls.homework_done[hw]
