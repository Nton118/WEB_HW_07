import argparse
from datetime import datetime, date, timedelta
from random import randint, choice
from typing import List
from sqlalchemy import select

from database.models import Teacher, Student, Discipline, Grade, Group
from database.db import session


parser = argparse.ArgumentParser(description='Простий CRUD для роботи з базою даних "Інститут"')
parser.add_argument("--action", "-a", choices=['create', 'list', 'update', 'remove'],
                    help="Дія яку потрібно виконати (create, list, update, remove)", required=True)
parser.add_argument("--model", "-m", choices=['Teacher', 'Student', 'Discipline', 'Grade', 'Group'],
                    help="модель, до якої застосовується дія", required=True)
parser.add_argument("--id", type=int, help="ідентифікатор запису", required=True)
parser.add_argument('--name', help="Ім'я запису")

args = parser.parse_args()



def seed_grades():
    start_date = datetime.strptime("2022-09-01", "%Y-%m-%d")
    finish_date = datetime.strptime("2023-05-31", "%Y-%m-%d")

    def get_list_date(start_date, finish_date) -> List[date]:
        result = []
        current_day: date = start_date
        while current_day < finish_date:
            if current_day.isoweekday() < 6:
                result.append(current_day)
            current_day += timedelta(1)
        return result

    list_date = get_list_date(start_date, finish_date)
    discipline_ids = session.scalars(select(Discipline.id)).all()
    student_ids = session.scalars(select(Student.id)).all()

    grades = []
    for day in list_date:
        random_subject_id = choice(discipline_ids)
        random_student_ids = [choice(student_ids) for _ in range(5)]
        for student_id in random_student_ids:
            grade = Grade(grade=randint(1, 12), date_of=day, student_id=student_id,
                          discipline_id=random_subject_id)
            session.add(grade)



if __name__ == "__main__":

    session.commit()