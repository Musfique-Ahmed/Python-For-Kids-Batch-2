# class Temparature:
#     def __init__(self,celsius):
#         self.celsius = celsius

#     @property
#     def farenheit(self):
#         return (self.celsius * 9/5) + 32
    

# t_1 = Temparature(-40) 
# print(t_1.farenheit)


class Rectangle:
    def __init__(self, l, w):
        self.l = l
        self.w = w

    @classmethod
    def info(cls):
        print("This is a rectangle, which has 4 sides")

    # @staticmethod
    # def area(l, w):
    #     print(f"The area of a rectangle is {l * w}")
    @property
    def area(self):
        print(f"The area of a rectangle is {self.l * self.w}")    

    def info2(self):
        print(f"This rectangle has length {self.l} and width {self.w}. The area is {self.l * self.w}")

Rectangle.info()              
Rectangle.area 

r1 = Rectangle(8, 4)          
r1.info2()