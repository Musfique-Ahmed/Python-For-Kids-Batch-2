class Circle:
    def __init__(self, r):
        self.r = r

    @classmethod
    def description(cls):
        print("This is a circle, which is round in shape!")

    @staticmethod
    def area(r):
        print(f"The area of the circle is {3.1416 * r**2}")

    def info(self):
        print(f"The radious of the circle is {self.r}")

Circle.description() 

Circle.area(5)

c_1 = Circle()
c_1.area(6)