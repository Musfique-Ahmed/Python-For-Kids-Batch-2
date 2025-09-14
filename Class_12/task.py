class Person:
    def __init__(self, name, age,  blood_grp):
        self.name = name
        self.age = age
        self.blood_grp = blood_grp

    def can_donate( self):
        print(f"{self.name} can donate {self.blood_grp} blood!")



class Student(Person):
    def __init__(self, name, age, blood_grp, id, grade, clas):
        super().__init__(name, age, blood_grp)
        self.id = id
        self.grade = grade
        self.clas = clas

    def info(self):
        print(f"Name: {self.name} \nID: {self.id}")


s1 = Student("Nusaybah", 12, 'B+', 11113, 5.00, 6)
s1.info()
s1.can_donate()