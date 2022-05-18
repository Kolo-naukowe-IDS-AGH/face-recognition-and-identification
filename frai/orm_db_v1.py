from select import select
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

from sqlalchemy import Column, Integer, String, Date
from sqlalchemy import ForeignKey

import pandas as pd

db_string = "mysql+pymysql://bargaw:BPmwPFhZi4jeiZ1P@mysql.agh.edu.pl:3306/bargaw"
Base = declarative_base()

class Student(Base):
        __tablename__ = 'student'
        id = Column(Integer, primary_key=True)
        name = Column(String(50))
        surname = Column(String(50))
        student_id_photo = Column(String(50))

        def __repr__(self):
            return "<student(id='{0}', name={1}, surname={2}, student_id_photo={3})>".format(
                self.id, self.name, self.surname, self.student_id_photo)

class Other_photos(Base):
    __tablename__ = 'other_photos'
    id = Column(Integer, primary_key=True)
    id_student = Column(Integer, ForeignKey('student.id'))
    photo_path = Column(String(50), nullable = False)
    
    def __repr__(self):
        return "<other_photos(id='{0}', id_student={1}, photo_path={2})>".format(
            self.id, self.id_student, self.photo_path)

class Method_1(Base):
    __tablename__ = 'method_1'
    id = Column(Integer, primary_key=True)
    id_student = Column(Integer, ForeignKey('student.id'))

    def __repr__(self):
        return "<other_photos(id='{0}', id_student={1})>".format(
            self.id, self.id_student)

class Method_2(Base):
    __tablename__ = 'method_2'
    id = Column(Integer, primary_key=True)
    id_student = Column(Integer, ForeignKey('student.id'))

    def __repr__(self):
        return "<other_photos(id='{0}', id_student={1})>".format(
            self.id, self.id_student)

class Method_3(Base):
    __tablename__ = 'method_3'
    id = Column(Integer, primary_key=True)
    id_student = Column(Integer, ForeignKey('student.id'))

    def __repr__(self):
        return "<other_photos(id='{0}', id_student={1})>".format(
            self.id, self.id_student)

class Method_4(Base):
    __tablename__ = 'method_4'
    id = Column(Integer, primary_key=True)
    id_student = Column(Integer, ForeignKey('student.id'))

    def __repr__(self):
        return "<other_photos(id='{0}', id_student={1})>".format(
            self.id, self.id_student)

def create_db():
    """
    Create database based on classes
    """
    try:
        engine = create_engine(db_string)
        engine.connect()
    except Exception as e:
        print('Can\'t connect to database')
        print('Error message:')
        print(e)
    else:
        print('Connected to database')
        Base.metadata.create_all(engine)

# create_db()

def add_records(table, rec_list):
    """
    Add records to chosen table.

    Parameters:
        rec_list (pandas.DataFrame or list)
        table (string)
    """
    if table not in list(Base.metadata.tables.keys()):
        mstr = f'There is no {table} table in database'
        raise ValueError(mstr)
    try:
        engine = create_engine(db_string)
        engine.connect()
    except Exception as e:
        print('Can\'t connect to database')
        print('Error message:')
        print(e)
    else:
        if type(rec_list) == list:
            with Session(engine) as session:
                for i in rec_list:
                    student = Student(name = i[0],
                                        surname = i[1],
                                        student_id_photo = i[2])
                    session.add(student)
                session.commit()

        elif type(rec_list) == pd.DataFrame:
            #TODO: TO BE IMPLEMENTED
            pass
        else:
            mstr = f'rec_list expected to be pandas.DataFrame or list. Instead it is {type(rec_list)}'
            raise TypeError(mstr)

add_records('student', [['a', 'aa', 'aaa'], ['b', 'bb', 'bbb']])