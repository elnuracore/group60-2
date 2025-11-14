class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def info(self):
        return f"Student {self.name}, age: {self.age}, GPA: {self.grade}"

    def improve_grade(self, value):
        self.grade += value


s1 = Student("Elnura", 19, 3.8)
s2 = Student("Aizhan", 20, 3.4)

print(s1.info())
print(s2.info())

s1.improve_grade(0.1)
s2.improve_grade(0.2)

print("After improvement:")
print(s1.info())
print(s2.info())
