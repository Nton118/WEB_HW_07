from datetime import datetime, date, timedelta
from random import randint, choice
from typing import List
from sqlalchemy import select
from faker import Faker

from database.models import Teacher, Student, Discipline, Grade, Group
from database.db import session

fake = Faker("uk-UA")

subjects = [
    "Математика",
    "Фізика",
    "Хімія",
    "Література",
    "Філософія",
    "Програмування",
    "Штучний інтелект",
    "Фінанси"]

groups = ["MM-01", "ПП-02", "АП-00"]

NUMBERS_TEACHERS = 5
NUMBERS_STUDENTS = 50


def seed_teachers():
    for _ in range(NUMBERS_TEACHERS):
        teacher = Teacher(fullname=fake.name())
        session.add(teacher)


def seed_groups():
    for group in groups:
        session.add(Group(name=group))


def seed_subjects():
    teacher_ids = session.scalars(select(Teacher.id)).all()
    for discipline in subjects:
        session.add(Discipline(name=discipline, teacher_id=choice(teacher_ids)))


def seed_students():
    group_ids = session.scalars(select(Group.id)).all()
    for _ in range(NUMBERS_STUDENTS):
        student = Student(fullname=fake.name(), group_id=choice(group_ids))
        session.add(student)


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


def fill_db():
    seed_teachers()
    seed_subjects()
    seed_groups()
    seed_students()
    seed_grades()
    session.commit()


if __name__ == "__main__":
    fill_db()
