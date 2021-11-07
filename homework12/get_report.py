import csv

from homework12.base import session
from homework12.create_table import HomeworkResult

with open("report.csv", "w") as f:
    out = csv.writer(f)
    out.writerow(["Student name", "Creation Date", "Teacher Name"])
    for item in session.query(HomeworkResult).filter_by(completed=True):
        out.writerow(
            [item.student.name, item.homework.created,
             item.homework.teacher.name]
        )
