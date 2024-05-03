import random

from faker import Faker
from sqlalchemy.exc import SQLAlchemyError

from conf.db import session
from conf.models import Grade, Teacher, Student, Group, Subject


fake = Faker("uk-UA")


def insert_groups():
    for _ in range(5):
        group = Group(name=fake.word())
        session.add(group)


def insert_students():
    for _ in range(50):
        groups = session.query(Group).all()
        student = Student(
            name=fake.name(),
            group_id=random.choice(groups).id,
            # last_name=fake.last_name(),
            # email=fake.email(),
            # phone=fake.phone_number(),
            # address=fake.address(),
        )
        session.add(student)


def insert_subjects():
    teachers = session.query(Teacher).all()
    for _ in range(8):
        subject = Subject(name=fake.word(), teacher_id=random.choice(teachers).id)
        session.add(subject)


def insert_teachers():
    for _ in range(6):
        teacher = Teacher(
            name=fake.name(),
        )
        session.add(teacher)


def insert_grades():
    students = session.query(Student).all()
    subjects = session.query(Subject).all()
    for student in students:
        for _ in range(random.randint(14, 20)):
            grade = Grade(
                student_id=student.id,
                subject_id=random.choice(subjects).id,
                grade=random.randint(1, 100),
                date=fake.date_between(start_date="-5M"),
            )
            session.add(grade)


# def insert_rel():
#     students = session.query(Student).all()
#     teachers = session.query(Teacher).all()

#     for student in students:
#         rel = TeacherStudent(
#             teacher_id=random.choice(teachers).id, student_id=student.id
#         )
#         session.add(rel)


if __name__ == "__main__":
    try:
        insert_groups()
        insert_students()
        # insert_teachers()
        # session.commit()
        # insert_rel()
        session.commit()
    except SQLAlchemyError as e:
        print(e)
        session.rollback()
    finally:
        session.close()
