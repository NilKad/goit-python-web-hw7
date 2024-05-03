from seeds.seeds import (
    insert_grades,
    insert_groups,
    insert_students,
    insert_subjects,
    insert_teachers,
)
from sqlalchemy.exc import SQLAlchemyError

from conf.db import session


if __name__ == "__main__":
    try:
        insert_groups()
        insert_students()
        insert_teachers()
        insert_subjects()
        session.commit()
        insert_grades()
        session.commit()
    except SQLAlchemyError as e:
        print(e)
        session.rollback()
    finally:
        session.close()
    pass
