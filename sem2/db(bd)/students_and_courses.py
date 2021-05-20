import sqlite3 as dbms
import random
conn = dbms.connect("students.sqlite3")  # Как оригинально!
cursor = conn.cursor()

with open("11.drop_ddl.sql", 'r', encoding='utf-8') as f:
    drop_ddl = f.read()
with open("11.create_ddl.sql", 'r', encoding='utf-8') as f:
    create_ddl = f.read()

if True:
    cursor.executescript(drop_ddl)
    conn.commit()
if True:
    cursor.executescript(create_ddl)
    conn.commit()

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
    programs_courses = relationship("Program_course", backref="program")

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
    marks = relationship("Mark", backref="student")
    
    def __init__(self, card, surname, name, patronymic, program):
        self.card = card
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.program = program
        
class Course(DeclBase):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    programs_courses = relationship("Program_course", backref="course")
    marks = relationship("Mark", backref="course")
    
    def __init__(self, name):
        self.name = name
        
class Program_course(DeclBase):
    __tablename__ = 'programs_courses'
    semester_number = Column(Integer, primary_key=True)
    
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)
    program_id = Column(Integer, ForeignKey('programs.id'), primary_key=True)
    
    def __init__(self, semester_number, course, program):
        self.semester_number = semester_number
        self.course = course
        self.program = program
        
class Mark(DeclBase):
    __tablename__ = 'marks'
    mark = Column(Integer)
    
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    
    def __init__(self, mark, student, course):
        self.mark = mark
        self.student = student
        self.course = course



#Конец содержательной части    
#Набор имен, фамилий, отчеств для создания студентов
Student_names_b = ["Александр","Алексей","Андрей","Антон","Артем","Борис","Богдан","Василий","Виктор","Владимир","Владислав","Всеволод","Георгий","Григорий","Геннадий","Дмитрий","Давид","Даниил","Данил","Данила","Егор","Евгений","Иван","Кирилл","Лев","Леонид","Максим","Михаил", "Макар","Никита","Николай","Олег","Петр","Павел","Родион","Роман","Семен","Сергей","Станислав","Тимофей","Федор","Эдуард","Юрий"]
Student_patronymics_b = ["Александрович","Алексеевич","Андреевич","Антонович","Артемович","Борисович","Васильевич","Викторович","Владимирович","Владиславович","Всеволодович","Георгиевич","Григорьевич","Геннадьевич","Дмитриевич","Давидович","Даниилович","Данилович","Данилович","Егорович","Евгеньевич","Иванович","Кириллович","Львович","Леонидович","Максимович","Михайлович", "Макарович","Никитич","Николаевич","Олегович","Петрович","Павлович","Родионович","Романович","Семенович","Сергеевич","Станиславович","Тимофеевич","Федорович","Эдуардович","Юрьевич"]
Student_patronymics_g = ["Александровна","Алексеевна","Андреевна","Антоновна","Артемовна","Борисовна","Васильевна","Викторовна","Владимировна","Владиславовна","Всеволодовна","Георгиевна","Григорьевна","Геннадьевна","Дмитриевна","Давидовна","Данииловна","Даниловна","Даниловна","Егоровна","Евгеньевна","Ивановна","Кирилловна","Львовна","Леонидовна","Максимовна","Михайловна", "Макаровна","Никична","Николаевна","Олеговна","Петровна","Павловна","Родионовна","Романовна","Семеновна","Сергеевна","Станиславовна","Тимофеевна","Федоровна","Эдуардовна","Юрьевна"]
Student_names_g = ["Александра","Анна","Алина","Алиса","Василиса","Валентина","Дарья","Евгения","Елена","Екатерина","Елизавета","Жанна","Зинаида","Инна","Исидора","Кристина","Мария","Милана","Наталья","Наталия","Ольга","Татьяна","Ульяна","Юлия"]
Student_surnames_b = ["Авдеев","Алексеев","Аверкиев","Антонов","Борисов","Васильев","Глухов","Дмитриев","Егоров","Ежов","Енотов","Барсуков","Жилин","Заречный","Игорев","Клюйков","Лазарев","Львов","Лопатин","Максимов","Михайлов","Непоклонов","Денисов","Обухов","Петров","Иванов","Сидоров","Свиридов"]
Student_surnames_g = ["Авдеевa","Алексеевa","Аверкиевa","Антоновa","Борисовa","Васильевa","Глуховa","Дмитриевa","Егоровa","Ежовa","Еотовa","Барсуковa","Жилинa","Заречная","Игорева","Клюйкова","Лазарева","Львова","Лопатина","Максимова","Михайлова","Непоклонова","Денисова","Обухова","Петрова","Иванова","Сидорова","Свиридова"]
                      


ph = Program("Физика")
pm = Program("Прикладная математика")


of = Course("Общая физика")
ch = Course("Химия")
vm = Course("Высшая математика")
al = Course("Алгебра")
an = Course("Матанализ")
pe = Course("Физкультура")
ps = Course("Философия")
fl = Course("Английский")

phc1of = Program_course("1", of, ph)
phc2of = Program_course("2", of, ph)
phc3of = Program_course("3", of, ph)
phc4of = Program_course("4", of, ph)

phc1vm = Program_course("1", vm, ph)
phc2vm = Program_course("2", vm, ph)

phc1pe = Program_course("1", pe, ph)
phc2pe = Program_course("2", pe, ph)
phc3pe = Program_course("3", pe, ph)
phc4pe = Program_course("4", pe, ph)

phc1ps = Program_course("1", ps, ph)
phc1ch = Program_course("1", ch, ph)

phc1fl = Program_course("1", fl, ph)
phc2fl = Program_course("2", fl, ph)
phc3fl = Program_course("3", fl, ph)
phc4fl = Program_course("4", fl, ph)#Студенты-физики

""""""

pmc1al = Program_course("1", al, pm)
pmc2al = Program_course("2", al, pm)
pmc3al = Program_course("3", al, pm)
pmc4al = Program_course("4", al, pm)

pmc1an = Program_course("1", an, pm)
pmc2an = Program_course("2", an, pm)
pmc3an = Program_course("3", an, pm)
pmc4an = Program_course("4", an, pm)

pmc1pe = Program_course("1", pe, pm)
pmc2pe = Program_course("2", pe, pm)
pmc3pe = Program_course("3", pe, pm)
pmc4pe = Program_course("4", pe, pm)

pmc1fl = Program_course("1", fl, pm)
pmc2fl = Program_course("2", fl, pm)
pmc3fl = Program_course("3", fl, pm)
pmc4fl = Program_course("4", fl, pm)

pmc1ps = Program_course("1", ps, pm)
pmc1ch = Program_course("1", ch, pm)#Студенты - математики

students_phys_math = []


for i in range (0,5):
    if random.choice([True,False]):
        students_phys_math.append(Student(str(100000+i),random.choice(Student_surnames_g),random.choice(Student_names_g),random.choice(Student_patronymics_g),ph))
    else:
        students_phys_math.append(Student(str(100000+i),random.choice(Student_surnames_b),random.choice(Student_names_b),random.choice(Student_patronymics_b),ph))
Ikari = Student("000003","Якорев","Сергей","Геннадьевич",ph)        
for i in range (0,3):
    if random.choice([True,False]):
        students_phys_math.append(Student(str(200000+i),random.choice(Student_surnames_g),random.choice(Student_names_g),random.choice(Student_patronymics_g),pm))
    else:
        students_phys_math.append(Student(str(200000+i),random.choice(Student_surnames_b),random.choice(Student_names_b),random.choice(Student_patronymics_b),pm))
       
session.add(pm)#Добавится сразу все! Наверное, причина - связность схемы базы данных.



session.add_all([pm])
session.commit()
mark_phys_math = []

for s in session.query(Student):
    prg = s.program
    for c in prg.programs_courses:
        if c.semester_number ==1 :#Чтобы не получить IntegrityError, 1 предмет - 1 оценка.
            if s.name == "Синдзи":
                m=Mark(random.choice([5]),s,c.course)#Он старался
                mark_phys_math.append(m)
            else:
                m=Mark(random.choice([2,3,4,4,4,4,4,4,5]),s,c.course)#Ставим случайные оценки
                mark_phys_math.append(m)
                

session.add_all([pm])
session.commit()




"""
ВЫВОД
"""



import sys

print("____________УЧЕБНЫЙ ПЛАН____________")
print("____________________________________")

for p in session.query(Program):
    
    print(p.name,":")
    print("Предмет   -   семестр")
    for pc in p.programs_courses:
        print (pc.course.name,"-",pc.semester_number)

    print("____________________________________")
    
print("____________________________________")
print("____________________________________")
print("____________________________________")

print("ОБЩАЯ УСПЕВАЕМОСТЬ:")
for sss in session.query(Student):
    print(sss.surname,sss.name,sss.patronymic,"получил:")
    for s in sss.marks:
        print(s.course.name,"- ", s.mark)
    print("____________________________________")




