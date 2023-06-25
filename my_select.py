from sqlalchemy import func, desc, and_, distinct, select
from sqlalchemy.orm import aliased

from database.models import Teacher, Student, Discipline, Grade, Group
from database.db import session


# Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
def select_1(*args):
    result = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()
    return result


# Знайти студента із найвищим середнім балом з певного предмета.
def select_2(n_subj):

    stmt = select(
        Discipline.name,
        Student.fullname,
        func.round(func.avg(Grade.grade), 2)).select_from(Grade).join(Student).join(Discipline).\
        where(Discipline.id == n_subj).group_by(Discipline.id, Student.fullname).\
        order_by(func.avg(Grade.grade).desc()).limit(1)
    result = session.execute(stmt).fetchone()
    return result


# Знайти середній бал у групах з певного предмета.
def select_3(n_subj):
    stmt = select(
        Group.name,
        Discipline.name,
        func.round(func.avg(Grade.grade), 2)).select_from(Grade).join(Student).join(Discipline).join(Group) \
        .where(Discipline.id == n_subj).group_by(Group.name, Discipline.name). \
        order_by(func.avg(Grade.grade).desc())
    result = session.execute(stmt).all()
    return result


# Знайти середній бал на потоці (по всій таблиці оцінок).
def select_4(*args):
    result = session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade).all()
    return result


# Знайти, які курси читає певний викладач
def select_5(t_id):
    result = session.query(Teacher.fullname, Discipline.name) \
        .select_from(Discipline).join(Teacher).where(Teacher.id == t_id).group_by(Teacher.id, Discipline.name).all()
    return result


# Знайти список студентів у певній групі
def select_6(n_gr):
    result = session.query(Student.fullname, Group.name) \
        .select_from(Student).join(Group).where(Group.id == n_gr).all()
    return result


# Знайти оцінки студентів в окремій групі з певного предмета.
def select_7(n_subj, n_gr):
    result = session.query(Group.name, Discipline.name, Student.fullname, Grade.grade) \
         .select_from(Grade).join(Student).join(Group).join(Discipline).where(and_(Discipline.id == n_subj,
         Group.id == n_gr)).all()
    return result


# Знайти середній бал, який ставить певний викладач зі своїх предметів
def select_8(teacher_id):
    result = session.query(distinct(Teacher.fullname), func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade) \
        .join(Discipline)  \
        .join(Teacher) \
        .where(Teacher.id == teacher_id).group_by(Teacher.fullname).all()
    return result


# Знайти список курсів, які відвідує певний студент
def select_9(n_st):
    result = session.query(Student.fullname, Discipline.name) \
        .select_from(Discipline).join(Grade).join(Student).where(Student.id == n_st) \
        .group_by(Discipline.name, Student.fullname).all()
    return result


# Список курсів, які певному студенту читає певний викладач
def select_10(n_st, n_teach):
    result = session.query(Discipline.name, Teacher.fullname, Student.fullname) \
        .select_from(Discipline).join(Grade).join(Student).join(Teacher) \
        .where(and_(Student.id == n_st, Teacher.id == n_teach)) \
        .group_by(Discipline.name, Student.fullname, Teacher.fullname).all()
    return result


# Середній бал, який певний викладач ставить певному студентові
def select_11(n_st, n_teach):
    result = session.query(Teacher.fullname, Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .select_from(Discipline).join(Teacher).join(Grade).join(Student) \
        .where(and_(Student.id == n_st, Teacher.id == n_teach)) \
        .group_by(Student.id, Teacher.id).all()
    return result


# Оцінки студентів у певній групі з певного предмета на останньому занятті
def select_12(group_id, dis_id):
    # Знаходимо останнє заняття
    subq = (select(Grade.date_of).join(Student).join(Group).where(
        and_(Grade.discipline_id == dis_id, Group.id == group_id)
    ).order_by(desc(Grade.date_of)).limit(1)).scalar_subquery()

    result = session.query(Student.fullname, Discipline.name, Group.name, Grade.grade, Grade.date_of) \
        .select_from(Grade) \
        .join(Student) \
        .join(Discipline) \
        .join(Group) \
        .filter(and_(Grade.discipline_id == dis_id, Group.id == group_id, Grade.date_of == subq)) \
        .order_by(desc(Grade.date_of)).all()
    return result


if __name__ == '__main__':
    # print(select_1())
    print(select_10(40, 2))
    # print(select_8(4))
    # print(select_12(2, 2))