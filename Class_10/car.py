class Car:
    def __init__(self,brand,model,color):
        self.brand=brand
        self.model=model
        self.color= color

    def askbrandname(self):
        print(f"the name of the brand is {self.brand} and the model is {self.model} ")
    def askcolor(self):
        print(f"my car is {self.color} color")


x_corolla = Car("Toyota", "X Corolla", "White")
x_corolla.askbrandname()
x_corolla.askcolor()




class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def display_info(self):
        print(f"My car is a {self.color} {self.brand} {self.model}.")


tesla = Car("Tesla", "Model S", "Black")
tesla.display_info()
