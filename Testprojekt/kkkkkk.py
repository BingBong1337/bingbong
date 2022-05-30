import random as r
import operator as op
class Employee():
    def __init__(self, name , age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({},{},{})'. format(self.name, self.age, self.salary)
    #def __str__(self):
    #    return '({},{},{})' . format(self.name, self.age, self.salray)
    def setage(self, newage):
        self.age = newage
        return

    def setname(self, newname):
        self.name = newname
        return

    def setsalary(self, newsalary):
        self.salary = newsalary

namn = ['Adam', 'Pär', 'Glenn', 'Johan']
e1 = Employee('','','')
e2 = Employee('','','')
e3 = Employee('','','')
e4 = Employee('','','')
def age():
    e1.age = r.randint(1,100)
    e2.age = r.randint(1,100)
    e3.age = r.randint(1,100)
    e4.age = r.randint(1,100)
def salary():
    e1.salary = r.randint(1000,100000)
    e2.salary = r.randint(1000,100000)
    e3.salary = r.randint(1000,100000)
    e4.salary = r.randint(1000,100000)

def name():
    e1.name = namn[(r.randint(0,3))]
    e2.name = namn[(r.randint(0,3))]
    e3.name = namn[(r.randint(0,3))]
    e4.name = namn[(r.randint(0,3))]
name()
age()
salary()



employees = []
if e1 not in employees:
    employees.append(e1)
if e1 in employees:
    employees.append(e2)
if e1 and e2 in employees:
    employees.append(e3)
if e1 and e2 and e3 in employees:
    employees.append(e4)
print(employees)
print(sorted(employees, key = op.attrgetter('salary'), reverse = True ))
