"""
Python Tutorial: https://docs.python.org/3/tutorial/classes.html
Classes
"""

class Person:
    # age = 0 --> no need to define those here... WFT
    # name = "" --> can use directly as self.new
    glo_surname = "General Surname"

    def __init__(self, p_age=None, p_name=None, occ=None):
        # self.glo_surname
        self.age = p_age
        self.name = p_name
        self.occupation = occ
        print(f'Hello: {self.name}, age {self.age}, occ. {self.occupation}')

    def do_stuff(self, p_work):
        self.work = p_work # not suggested, __init__
        self.glo_surname = p_work
        # print(f'surname: {self.glo_surname}')
        print(self.work)

class Employee(Person):
    def __init__(self, e_age, e_name):
        self.occupation = "Employee"
        Person.__init__(self, e_age, e_name, self.occupation)
        print(f'employee created {self.age} {self.name} {self.occupation}')

    def do_stuff(self, p_work):
        Person.do_stuff(self, p_work)
        print("EXTRA OT WORK...")

p1 = Person()
p2 = Person(34, "Stas")

# print(p2.occupation)
# p1.do_stuff("doing doing doing")
# p2.do_stuff("work work work")
print("\n")
e1 = Employee(55, "Nel")
e1.do_stuff("ot ot ot ot ")
print("\n")

print(isinstance(e1, Person))
print(isinstance(e1, Employee))
print(issubclass(Employee, Person))
print(issubclass(Person, Employee))

