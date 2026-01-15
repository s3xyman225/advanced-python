class Person:
    def __init__(self, name):   
        self._name = name

    def info(self):
        return f"Name: {self._name}"


class Student(Person):
    def info(self):
        return f"Student name: {self._name}"


people = [
    Person("Bob"),
    Student("Nazar")
]

for p in people:
    print(p.info())
