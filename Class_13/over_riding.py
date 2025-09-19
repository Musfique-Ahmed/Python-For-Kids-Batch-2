#parent class
class Bird:
    def fly(self):
        pass

#child class
class Eagle(Bird):
    def fly(self):
        return "can fly"
    
class Penguin(Bird):
    def fly(self):
        return "cannot fly"