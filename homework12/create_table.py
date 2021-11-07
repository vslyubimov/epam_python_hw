from collections import defaultdict
from datetime import datetime, timedelta

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from homework12.base import Base, engine, session
from homework6.task02 import DeadlineError


class Homework(Base):
    __tablename__ = "Homeworks"
    id = Column(Integer, primary_key=True)
    text = Column(String, unique=True)
    teacher_id = Column(Integer, ForeignKey("Teachers.id"))
    teacher = relationship("Teacher")
    created = Column(DateTime, default=datetime.now())
    deadline = Column(DateTime)

    def is_active(self) -> bool:
        return datetime.today() <= self.deadline


class Student(Base):
    __tablename__ = "Students"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    last_name = Column(String(50))

    def do_homework(self, todo, solution):
        if todo.is_active():
            h_res = HomeworkResult(solution=solution,
                                   student=self, homework=todo)
            session.add(h_res)
            session.commit()
            return h_res
        raise DeadlineError


class HomeworkResult(Base):
    __tablename__ = "HomeworkResults"
    id = Column(Integer, primary_key=True)
    solution = Column(String(50), unique=True)
    student_id = Column(Integer, ForeignKey("Students.id"))
    student = relationship("Student", foreign_keys=[student_id])
    homework_id = Column(Integer, ForeignKey("Homeworks.id"))
    homework = relationship("Homework", foreign_keys=[homework_id])
    completed = Column(Boolean)


class Teacher(Base):
    __tablename__ = "Teachers"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    last_name = Column(String(50))
    homework_done = defaultdict(list)

    def create_homework(self, text, deadline):
        hw = Homework(
            text=text, deadline=datetime.now() + timedelta(deadline),
            teacher=self
        )
        session.add(hw)
        session.commit()
        return hw

    @classmethod
    def check_homework(cls, checking):
        checking.completed = len(checking.solution) >= 5
        session.commit()
        return checking.completed

    @classmethod
    def reset_results(cls, hw):
        if hw is None:
            cls.homework_done.clear()
        else:
            del cls.homework_done[hw]


if __name__ == "__main__":
    Base.metadata.create_all(engine)
