# databases start,
# SQL
# Object oriented programming

class Person:
    age = 0
    name = ""

    def __init__(self, n):
        self.name = n
        print('constructed: ', self.name, self.age)

    def __del__(self):
        print('destructed: ', self.name, self.age)

    def sayhello(self):
        print('Hello', self.name)



class Employee(Person):
    salary = 0.0

    def getsalary(self, s):
        self.salary = s
        print("salary", self.salary)


if __name__ == "__main__":
    p = Person("Stasiek")
    p.sayhello()

    e = Employee("Jozek")
    e.getsalary(300)
    e.sayhello()
