from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Integer, String, Date
from sqlalchemy import ForeignKey

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

# def connect(db_string="mysql+pymysql://bargaw:BPmwPFhZi4jeiZ1P@mysql.agh.edu.pl:3306/bargaw"):


# from sqlalchemy_utils import database_exists, create_database

# if not database_exists(engine.url):
#     create_database(engine.url)
# else:
#     # Connect the database if exists.
#     engine.connect()
#     Base.metadata.create_all(engine)