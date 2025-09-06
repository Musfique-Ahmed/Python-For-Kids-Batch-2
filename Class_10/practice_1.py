# class Animal:
#     def __init__(self, name, sound, leg=4):
#         self.name = name
#         self.sound = sound
#         self.leg = leg

#     def make_sound(self):
#         print(f"{self.name} says {self.sound}")

#     def walking(self):
#         print(f"{self.name} is walking on {self.leg} legs")

 

# dog = Animal("Dog", "Woof")
# dog.make_sound()
# dog.walking()

# cat = Animal("Cat", "Meawo")
# cat.make_sound()
# cat.walking()

# cow = Animal("Cow", "Mooo")
# cow.make_sound()
# cow.walking()

# bear = Animal("Bear", "Rawr", 2)
# bear.make_sound()
# bear.walking()







class Student:
    def __init__(self, name, age, id, level, cgpa):
        #Attributes
        self.name = name
        self.age = age
        self.id = id
        self.level = level
        self.cgpa = cgpa

    #Methods
    def introduce(self):
        print(f"Hello, my name is {self.name}. \nI read in class {self.level}. \nI am {self.age} years old.")

    def ask_id(self):
        print(f"My id is {self.id}")

    def ask_cgpa(self):
        print(f"My CGPA is {self.cgpa}")

#Object for the class
stu_1 = Student("Msufique", 21, "01523330101", 14, 5.00)
stu_1.introduce()
stu_1.ask_id()
stu_1.ask_cgpa()