from sqlalchemy import and_, func, desc


from conf.db import session
from conf.models import Student, Teacher, Group, Subject, Grade


def select_1():
    sel = (
        session.query(
            Student.id,
            Student.name,
            func.round(func.avg(Grade.grade), 6).label("avg_grade"),
        )
        .select_from(Student)
        .join(Grade, Grade.id == Student.id)
        .group_by(Student.id)
        .order_by(desc("avg_grade"))
        .limit(5)
        .all()
    )
    return sel


def select_2(subject_id):
    sel = (
        session.query(
            Student.id,
            Student.name,
            func.round(func.avg(Grade.grade), 2).label("avg_grade"),
        )
        .select_from(Student)
        .join(Grade, Grade.student_id == Student.id)
        .filter(Grade.subject_id == subject_id)
        .group_by(Student.id)
        .order_by(desc("avg_grade"))
        .limit(1)
        .all()
    )
    return sel


def select_3(subject_id):
    sel = (
        session.query(
            Group.id,
            Group.name,
            func.round(func.avg(Grade.grade), 2).label("avg_grade"),
        )
        .select_from(Group)
        .join(Student, Student.group_id == Group.id)
        .join(Grade, Grade.student_id == Student.id)
        .filter(Grade.subject_id == subject_id)
        .group_by(Group.id)
        .all()
    )
    return sel


def select_4():
    sel = session.query(func.round(func.avg(Grade.grade), 2).label("avg_grade")).all()
    return sel


def select_5(teacher_id):
    sel = (
        session.query(Subject.id, Subject.name)
        .filter(Subject.teacher_id == teacher_id)
        .all()
    )
    return sel


def select_6(group_id):
    sel = session.query(Student.id, Student.name).filter(Group.id == group_id).all()
    return sel


def select_7(group_id, subject_id):
    sel = (
        session.query(Student.id, Student.name, Grade.grade)
        .join(Grade, Grade.student_id == Grade.student_id)
        # .filter(Student.group_id == group_id)
        # .filter(
        #     Grade.subject_id == subject_id,
        # )
        .filter(and_(Student.group_id == group_id, Grade.subject_id == subject_id))
        .all()
    )
    return sel


def select_8(teacher_id):
    sel = (
        session.query(Subject.id, Subject.name, func.round(func.avg(Grade.grade), 2))
        .join(Grade, Grade.subject_id == Subject.id)
        .filter(Subject.teacher_id == teacher_id)
        .group_by(Subject.id)
        .all()
    )
    return sel


def select_9(student_id):
    sel = (
        session.query(Subject.id, Subject.name)
        .select_from(Subject)
        .join(Grade, Grade.subject_id == Subject.id)
        .filter(Grade.student_id == student_id)
        .group_by(Subject.id)
        .all()
    )
    return sel


def select_10(student_id, teacher_id):
    sel = (
        session.query(Subject.id, Subject.name)
        .join(Grade, Grade.student_id == student_id)
        # .filter(Grade.student_id == 1)
        .filter(Subject.teacher_id == teacher_id)
        .group_by(Subject.id)
        .all()
    )
    return sel


def select_adv_1(teacher_id, student_id):
    sel = (
        session.query(func.round(func.avg(Grade.grade), 2))
        .select_from(Grade)
        .join(Subject, Subject.teacher_id == teacher_id)
        .filter(Grade.student_id == student_id)
        .scalar()
    )
    return sel


def select_adv_2(group_id, subject_id):
    max_date_subquery = (
        session.query(func.max(Grade.date))
        .join(Student)
        .filter(Student.group_id == group_id, Grade.subject_id == subject_id)
        .correlate(Student)
        .as_scalar()
    )
    sel = (
        session.query(Student.id, Student.name, Grade.grade, Grade.date)
        .select_from(Grade)
        .join(Student, Student.id == Grade.student_id)
        .filter(
            and_(
                Student.group_id == group_id,
                Grade.subject_id == subject_id,
                Grade.date == max_date_subquery,
            )
        )
    ).all()
    return sel


if __name__ == "__main__":
    # print(select_1())
    # print(select_2(1))
    # print(select_3(1))
    # print(select_4())
    # print(select_5(1))
    # print(select_6(1))
    # print(select_7(1, 2))
    # print(select_8(4))
    # print(select_9(2))
    # print(select_10(1, 3))
    # print(select_adv_1(1, 4))
    print(select_adv_2(1, 2))
