# class Animal:
#     def __init__(self, id, legs):
#         self.id = id
#         self.legs = legs

#     def breathe(self):
#         return f"Breathing....."
    


# class Dog(Animal):
#     def __init__(self,id, legs , name):
#         # Call the parent's __init__ method to set id, legs
#         super().__init__(id, legs)
#         self.name = name

#     def bark(self):
#         return f"Woof! Woof!"
    


# dog = Dog(12, 3, "Tomy")
# print(dog.breathe())
# print(dog.bark())
# print(dog.legs)







class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        return f"I am a {self.name} and I am {self.age} years old."

class Cat(Animal):
    def __init__(self, name, age, color):
        # Call the parent's __init__ method to set name and age
        super().__init__(name, age)
        # Add a new attribute specific to Cat
        self.color = color

    def show_info(self):
        # Call the parent's show_info method and add to it
        base_info = super().show_info()
        return f"{base_info} My fur is {self.color}."

# Create a Cat object
my_cat = Cat("Whiskers", 5, "black")
print(my_cat.show_info())
# Output: I am a Whiskers and I am 5 years old. My fur is black.