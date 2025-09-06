# # class Car:
# #     #class variable
# #     wheel = 4
# #     # common gulor khetre amra class variable use kori

# #     # Methods
# #     def __init__(self, mdoel, color, engine, brand):
# #         # instance variable
# #         self.model = mdoel
# #         self.color = color
# #         self.engine = engine
# #         self.brand = brand
# #         # jegulo prottekta instance onujai change hobe, shegulor jonno instance variable use korbo




# class student:
#     school_name = "ABC High School"

#     def __init__(self, name,grade):
#         self.name= name
#         self.grade= grade

#     def info(self):
#         print(f"{self.name} is in {self.grade}, studing in {self.school_name}")
    
# person=student("Daniel", "class 9")
# person.info()


class Student:
    school_name = "abc high school"  

    def __init__(self, name, grade): 
        self.name = name              
        self.grade = grade   

    @classmethod
    def description(cls):
        print("This is the ABC high school!")         

    def display_info(self): #instance method          
        print(f"School: {Student.school_name}")
        print(f"Name: {self.name}")
        print(f"Grade: {self.grade}")


person=Student("Daniel", "class 9")
person.display_info()
person.description()

Student.description()
# Student.display_info()