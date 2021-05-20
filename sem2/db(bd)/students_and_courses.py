import sqlite3 as dbms
conn = dbms.connect("students.sqlite3")  # Как оригинально!
cursor = conn.cursor()
with open("11.drop_ddl.sql", 'r', encoding='utf-8') as f:
    drop_ddl = f.read()
with open("11.create_ddl.sql", 'r', encoding='utf-8') as f:
    create_ddl = f.read()
with open("11.insert_dml.sql", 'r', encoding='utf-8') as f:
    insert_dml = f.read()
if True:
    cursor.executescript(drop_ddl)
    conn.commit()
if True:
    cursor.executescript(create_ddl)
    conn.commit()
if True:
    cursor.executescript(insert_dml)
conn.commit()


from IPython.display import HTML, display
import tabulate  # pip install tabulate

cursor.execute(
    '''select id, name from programs'''
)
display(HTML(tabulate.tabulate(cursor.fetchall(), tablefmt='html')))

cursor.execute(
    '''select programs.name, students.name, surname, patronymic
    from programs join students
    on programs.id = program_id''')

display(HTML(tabulate.tabulate(cursor.fetchall(), tablefmt='html')))




name = "Василий"
surname = "Пупкин"
card = '199099'
cursor.execute(
    "insert into students(program_id, card, surname, name) values(1, ?, ?, ?)",
    (card, surname, name)
)
conn.commit()
conn.close()


import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

DeclBase = declarative_base()

engine = sqlalchemy.create_engine('sqlite:///students.sqlite3', echo=False)  # echo=True для логгинга
Session = sessionmaker(bind=engine)
session = Session()

class Program(DeclBase):
    __tablename__ = 'programs'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    students = relationship("Student", backref="program")
   

    def __init__(self, name):
        self.name = name

class Student(DeclBase):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    card = Column(String)
    surname = Column(String)
    name = Column(String)
    patronymic = Column(String)
    
    program_id = Column(Integer, ForeignKey('programs.id'))
    
    def __init__(self, card, surname, name, patronymic, program):
        self.card = card
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.program = program

        
class Course(DeclBase):
    __tablename__  = 'courses'
    id = Column (Integer, primary_key = True)
    name = Column(String)

    def __init__ (self, name):
        self.name = name


class Mark(DeclBase):
    __tablename__ = 'marks'
    student_id = Column(Integer,ForeignKey('students.id'))
    course_id = Column(Integer,ForeignKey('courses.id'))
    mark = Column(String)

    def __init__(self,student,mark,course):
        self.mark = mark
        self.student = student
        self.course = course



c = Course("Философия")

    
    





    
se = Program("Программная инженерия")

st1 = Student("002002", "Иванов", "Пётр", "Сидорович", se)
st2 = Student("002003", "Петрова", "Исидора", "Ивановна", se)

session.add_all([st1, st2])  # se само
session.commit()


m = Mark(st1,"хор.", c)




"""вывод"""
import sys

print("Программы и студенты")
for p in session.query(Program):
    print("Программа: ", p.name)
    for s in p.students:
        print("- ", s.name)

pr = session.query(Program).filter_by(name="теоретическая физика")[0]
st = session.query(Student).filter_by(name="Исидора")[0]

st.program = pr
session.commit()

print("Программы и студенты")
for p in session.query(Program):
    print("Программа: ", p.name)
    for s in p.students:
        print("- ", s.name)







