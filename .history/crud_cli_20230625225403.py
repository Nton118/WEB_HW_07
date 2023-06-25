import argparse
from datetime import datetime, date, timedelta
from random import randint, choice
from typing import List
from sqlalchemy import select

from database.models import Teacher, Student, Discipline, Grade, Group
from database.db import session
from main import count_records

parser = argparse.ArgumentParser(description='Простий CRUD для роботи з базою даних "Інститут"')
parser.add_argument("--action", "-a", choices=['create', 'list', 'update', 'remove'],
                    help="Дія яку потрібно виконати (create, list, update, remove)", required=True)
parser.add_argument("--model", "-m", choices=['Teacher', 'Student', 'Discipline', 'Grade', 'Group'],
                    help="модель, до якої застосовується дія", required=True)
parser.add_argument("--id", type=int, help="ідентифікатор запису", required=True)
parser.add_argument('--name', help="Ім'я запису", required=True)
parser.add_argument('--date_of', help="дата для оцінки", required=True)
parser.add_argument('--student_id', help="ID студента для оцінки", required=True)
parser.add_argument('--discipline_id', help="ID предмета для оцінки", required=True)
parser.add_argument('--group_id', help="ID групи для студента")
parser.add_argument('--teacher_id', help="ID викладача для предмета")

args = parser.parse_args()

if not args.action or not args.model:
    parser.error('Обидва аргументи --action та --model необхідні')

# Виконання CRUD операції залежно від переданого варіанту дії і моделі
if args.model == 'Teacher':
    if args.action == 'create':

        teacher = Teacher(name=args.name)
        session.add(teacher)
        session.commit()
        print('Викладача створено успішно.')

    elif args.action == 'list':

        teachers = session.query(Teacher).all()
        for teacher in teachers:
            print(f"Викладач з ID: {teacher.id}, Ім'я: {teacher.name}")

    elif args.action == 'update':

        teacher = session.query(Teacher).get(args.id)
        if teacher:
            teacher.name = args.name
            session.commit()
            print(f'Викладач з ID {args.id} успішно змінений.')
        else:
            print(f'Викладач з ID {args.id} не існує.')

    elif args.action == 'remove':

        teacher = session.query(Teacher).get(args.id)
        if teacher:
            session.delete(teacher)
            session.commit()
            print(f'Вчителя з ID {args.id} успішно видалено.')
        else:
            print(f'Вчитель з ID {args.id} не існує.')

elif args.model == 'Group':
    if args.action == 'create':

        group = Group(name=args.name)
        session.add(group)
        session.commit()
        print('Групу створено успішно.')

    elif args.action == 'list':

        groups = session.query(Group).all()
        for group in groups:
            print(f'Група з ID: {group.id}, Назва: {group.name}')

    elif args.action == 'update':

        group = session.query(Group).get(args.id)
        if group:
            group.name = args.name
            session.commit()
            print(f'Група з ID {args.id} успішно змінена.')
        else:
            print(f'Група з ID {args.id} не існує.')

    elif args.action == 'remove':

        group = session.query(Group).get(args.id)
        if group:
            session.delete(group)
            session.commit()
            print(f'Групу з з ID {args.id} успішно видалено.')
        else:
            print(f'Група з ID {args.id} не існує.')

elif args.model == 'Discipline':
    if args.action == 'create':

        discipline = Discipline(name=args.name, teacher_id=choice(count_records(Teacher)) if not args.teacher_id else args.teacher_id)
        session.add(discipline)
        session.commit()
        print('Предмет створено успішно.')

    elif args.action == 'list':

        disciplines = session.query(Discipline).all()
        for discipline in disciplines:
            print(f'Предмет з ID: {discipline.id}, Назва: {discipline.name}')

    elif args.action == 'update':

        discipline = session.query(Discipline).get(args.id)
        if discipline:
            discipline.name = args.name
            session.commit()
            print(f'Предмет з ID {args.id} успішно змінений.')
        else:
            print(f'ГПредмет з ID {args.id} не існує.')

    elif args.action == 'remove':

        discipline = session.query(Discipline).get(args.id)
        if discipline:
            session.delete(discipline)
            session.commit()
            print(f'Предмет з з ID {args.id} успішно видалено.')
        else:
            print(f'Предмет з ID {args.id} не існує.')

elif args.model == 'Student':
    if args.action == 'create':

        student = Student(name=args.name, group_id=choice(count_records(Group)) if not args.group_id else args.group_id)
        session.add(student)
        session.commit()
        print('Студента створено успішно.')

    elif args.action == 'list':

        students = session.query(Student).all()
        for student in students:
            print(f"Студент з ID: {student.id}, Ім'я: {student.name}")

    elif args.action == 'update':

        student = session.query(Student).get(args.id)
        if student:
            student.name = args.name
            session.commit()
            print(f'Студента з ID {args.id} успішно змінений.')
        else:
            print(f'Студент з ID {args.id} не існує.')

    elif args.action == 'remove':

        student = session.query(Student).get(args.id)
        if student:
            session.delete(student)
            session.commit()
            print(f'Студента з з ID {args.id} успішно видалено.')
        else:
            print(f'Студент з ID {args.id} не існує.')

elif args.model == 'Grade':
    if args.action == 'create':

        grade = Grade(name=args.name, group_id=choice(count_records(Group)) if not args.group_id else args.group_id)
        session.add(student)
        session.commit()
        print('Студента створено успішно.')

    elif args.action == 'list':

        grades = session.query(Grade).all()
        for student in students:
            print(f"Студент з ID: {student.id}, Ім'я: {student.name}")

    elif args.action == 'update':

        grade = session.query(Grade).get(args.id)
        if grade:
            grade.пкфву = args.name
            session.commit()
            print(f'Студента з ID {args.id} успішно змінений.')
        else:
            print(f'Студент з ID {args.id} не існує.')

    elif args.action == 'remove':

        student = session.query(Grade).get(args.id)
        if student:
            session.delete(student)
            session.commit()
            print(f'Студента з з ID {args.id} успішно видалено.')
        else:
            print(f'Студент з ID {args.id} не існує.')
            
else:
    parser.error('Заданої моделі не існує.')

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