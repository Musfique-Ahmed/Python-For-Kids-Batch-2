# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance


# n_0057 = BankAccount("Nusaybah", 1000)

# print(n_0057.balance)
# n_0057.balance = 20000000000


# print(n_0057.balance)


# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         #Encapsulation
#         self.__balance = balance #Private variable

#     #Getter Method
#     def get_balance(self):
#         print(f"Your current balance: {self.__balance} BDT")

#     # Updateing a private variable
#     def deposite(self, amount):
#         self.__balance += amount
#         print(f"Your transaction was successful! \ncurrent balance: {self.__balance} BDT")

#     def withdraw(self, amount):
#         self.__balance -= amount
#         print(f"Your transaction was successful! \ncurrent balance: {self.__balance} BDT")


# n_0057 = BankAccount("Nusaybah", 1000)


# n_0057.get_balance()
# # n_0057.get_balance() = 20000000000
# # n_0057.get_balance()
# n_0057.deposite(3500)


# n_0057.withdraw(2000)


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.__grade = grade 

    def get_grade(self):
        "Safely return the student's grade"
        return self.__grade

s1 = Student("Ali", "A")
print(s1.name)          
# print(s1.__grade())
print(s1.get_grade())