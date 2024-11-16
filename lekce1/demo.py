class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ma {self.age} years old"


class Student(Person):
    students_moto = "Study study study"

    def __init__(self, name, age, scholarship):
        Person.__init__(self, name, age)
        self.scholarship = scholarship

    def show_finance(self):
        return self.scholarship

    @classmethod
    def alter_moto(cls, new_moto):
        cls.students_moto = new_moto

    @classmethod
    def create_from_string(cls, inscription):
        name, age, scholarship = inscription.split()
        age, scholarship = int(age), float(scholarship)
        if cls.is_name_correct(name):
            return cls(name, age, scholarship)

    @staticmethod
    def is_name_correct(name):
        if name[0].isupper() and len(name) > 3:
            return True
        return False


stud1 = Student("Margaret", 32, 0)
stud2 = Student.create_from_string("Mark 21 600")
print(stud1.students_moto)
stud1.alter_moto("Do not study")
print(stud1.students_moto)
print(stud2.students_moto)
print(stud1.is_name_correct("alice"))
