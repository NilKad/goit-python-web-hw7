from sqlalchemy import (
    CheckConstraint,
    Column,
    Date,
    Integer,
    String,
    ForeignKey,
    func,
)
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.ext.hybrid import hybrid_property

Base = declarative_base()


class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    group_id = Column(
        Integer, ForeignKey("groups.id", ondelete="SET NULL", onupdate="CASCADE")
    )


class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))


class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    teacher_id = Column(
        Integer, ForeignKey("teachers.id", ondelete="SET NULL", onupdate="CASCADE")
    )


class Grade(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True)
    student_id = Column(
        Integer, ForeignKey("students.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    subject_id = Column(
        Integer, ForeignKey("subjects.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    grade = Column(
        Integer,
    )
    date = Column(Date, nullable=False)

    __table_args__ = (CheckConstraint("grade >= 1"), CheckConstraint("grade <= 100"))
