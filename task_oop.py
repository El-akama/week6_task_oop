# task1

# class Student:
#     """student information"""
#     def __init__(self, name, lastname, department, year_of_entrance):
#         self.name = name
#         self.lastname = lastname
#         self.department = department
#         self.year_of_entrance = year_of_entrance

#     def get_student_info(self):
#         print(f"{self.name} {self.lastname} поступил в {self.year_of_entrance} г. на факультет: {self.department}.")

# study = Student('Вася', "Иванов", "Программирование", "2017")
# study.get_student_info()


# task2

# class BankAccount:
#     """information of Bank's Account"""
#     balance = 0

#     def withdraw(self, amount):
#         self.balance -= amount
#         if self.balance > 0:
#             return self.balance
#         else:
#             return 'babla net'

#     def deposit(self, amount):
#         self.balance += amount
#         return self.balance

# bank = BankAccount()
# bank.balance = 15000
# m = bank.withdraw(15500)
# p = bank.deposit(1000)
# print(f'у вас на карте {m}')
# print(f"с учетом депозита {p}")

# task3

# class Airplane:
#     """black box of airplane"""
#     def __init__(self, make, model, year, max_speed):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.max_speed = max_speed
#         self.odometer = 0
#         self.is_flying = False

#     def take_off(self):
#         self.is_flying = True
#         info_take = f"{self.make} {self.model} взлетел в {self.year}г."
#         return info_take

#     def fly(self, km):
#         self.odometer += km
#         info_fly = f"{self.make} пролетел {self.odometer}км со скоростью {self.max_speed} км/ч."
#         return info_fly

#     def land(self):
#         self.is_flying = False
#         info_land = f"{self.make} приземлился, одометр показал {self.odometer}км."
#         return info_land
# point = Airplane("Миг", "24", "2020", 2000)
# print(point.take_off())
# print(point.fly(600))
# print(point.fly(600))
# print(point.land())