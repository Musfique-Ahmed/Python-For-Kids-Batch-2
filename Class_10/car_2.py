class Car:
    def __init__(self,brand,model,color,yearmade,numofdoors,enginesize,manufacturersname, price):
        self.brand=brand
        self.model=model
        self.color= color
        self.yearmade=yearmade
        self.manufacturersname= manufacturersname
        self.enginesizee=enginesize
        self.numofdoors=numofdoors
        self.price = price

    def ask1(self):
        print(f"the name of the brand is {self.brand} and the model is {self.model} ")
    def ask2(self):
        print(f"my car is {self.color} color and there r {self.numofdoors} doors")
    def ask3(self):
        print(f"it was made in year{self.yearmade} and the engine size is {self.enginesizee}")

    def change_color(self, new_color):
        self.color = new_color

    def calculate_cost(self):
        tax = float(self.enginesizee.strip("L"))
        self.price += (10000*tax)
        print(f"The price for this car is: {self.price}")

    


carr= Car("Toyota", "X Corolla", "White","2000","4","3.6L", "Toyota", 6000000)
carr.ask1()
carr.ask2()
carr.ask3()
carr.change_color("Red")
carr.ask2()
carr.calculate_cost()
