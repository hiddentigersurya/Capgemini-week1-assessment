# 1
# class Employee:
#     def __init__(self,name,id,department):
#         self.name=name
#         self.id=id
#         self.department=department
#     def show(self):
#         print(f'Name: {self.name} \nID: {self.id} \nDepartment: {self.department}')
# name=input("Enter your name:")
# ID=input("Enetr your ID:")
# department=input('Enter your department:')
# emp1=Employee(name,ID,department)
# emp1.show()
#------------------------------------------------------------------
#2
# class BankAccount:
#     def __init__(self):
#         self.balance=10000
#     def deposit(self,amount):
#         self.balance+=amount
#     def withdraw(self,amount):
#         if(self.balance<amount):
#             print("Insufficient funds in your account")
#         else:
#             self.balance-=amount

# acc1=BankAccount()
# print('Enter 1.deposit, 2.withdraw')
# option=int(input("Enter the option: "))
# if(option==1):
#     amount=int(input('Enter the amount for deposit: '))
#     acc1.deposit(amount)
#     print(f'Your account balance is {acc1.balance}')
# elif(option==2):
#     amount=int(input('Enter the amount to withdraw: '))
#     acc1.withdraw(amount)
#     print(f'Your account balance is {acc1.balance}')
# else:
#     print("Your transaction is cancelled")
#------------------------------------------------------------
#3
# class Library:
#     def __init__(self,title,author,isbn):
#         # self.books={}
#         self.title=title
#         self.author=author
#         self.isbn=isbn
#         # self.books[isbn]={'name':self.title,'author':self.author,'ISBN':self.isbn}
#     def display(self):
#         # for i in self.books.values():
#         #     print(i)
#         print(f"Title:{self.title}\nAuthor:{self.author}\nISBN:{self.isbn}")
# print("Enter the Book Details")
# title=input('Enter the book title:')
# author=input('Enter the author of the book:')
# isbn=input("Enter the isbn of the book:")
# lib=Library(title,author,isbn)
# lib.display()
#----------------------------------------
#4
# class Student:
#     def __init__(self,name,rollno):
#         self.name=name
#         self.rollno=rollno
#     def student_details(self):
#         return {'name':self.name,'roll no':self.rollno}
# student1=Student('durga','5f6')
# print(student1.student_details())
#---------------------------------------------------------------
#5
# class Product:
#     def __init__(self,name,price,stock):
#         self.name=name
#         self.price=price
#         self.stock=stock
#     def check_availability(self,quantity):
#         if(quantity>self.stock):
#             return f'{self.name} is not available'
#         else:
#             return f'{self.name} is available'
# prod=Product('Dal',80,20)
# print(prod.check_availability(30))
#--------------------------------------------------------------
#Inheritance
#6.
# class Vehicle:
#     def __init__(self,vehicle_number,brand):
#         self.vehicle_number=vehicle_number
#         self.brand=brand
#     def start_engine(self):
#         print("The engine has started")
# class Bike(Vehicle):
#     def __init__(self, vehicle_number, brand):
#         super().__init__(vehicle_number,brand)
#     def open_petroltank(self):
#         print("Ready to fill petrol")
#     def display(self):
#         print(f'brand:{self.brand}, vehicle number:{self.vehicle_number}')
# class Car(Vehicle):
#     def __init__(self, vehicle_number,fuel_type,brand):
#         super().__init__(vehicle_number, brand)
#         self.fuel_type=fuel_type
#     def open_boot(self):
#         print("The boot is opened")
#     def display(self):
#         print(f'brand:{self.brand}, vehicle number:{self.vehicle_number} and fuel type:{self.fuel_type}')
# class Electriccar(Car):
#     def __init__(self, vehicle_number, fuel_type,brand,capacity):
#         super().__init__(vehicle_number,  brand,fuel_type)
#         self.capacity=capacity
#     def display(self):
#         print(f'brand:{self.brand}, vehicle number:{self.vehicle_number}, and Capacity:{self.capacity}KWH')
# car1=Car(1221,'petrol','suzuki')
# car1.open_boot()
# car1.start_engine()
# car1.display()
# ecar=Electriccar(1234,'mahidra','electric',500)
# ecar.display()
# ecar.start_engine()
# bike=Bike(23444,'pulsur')
# bike.open_petroltank()
# bike.display()
#------------------------------------------------------------
#7. Create a multi-level class structure with `Person` → `Employee` → `Manager`, 
# where `Manager` has an additional method `approve_leave()`.
# class Person:
#     def __init__(self,name):
#         self.name=name
#     def display(self):
#         print(f'Name:{self.name}')
# class Employee(Person):
#     def __init__(self, name,id):
#         super().__init__(name)
#         self.id=id
#     def display(self):
#         print(f'The employee id is:{self.id}')
#         super().display()
# class Manager(Employee):
#     def __init__(self, name, id,department):
#         super().__init__(name, id)
#         self.department=department
#     def approve_leave(self):
#         print("The leave has been approved")
#     def display(self):
#         print(f'The manager department:{self.department}')
#         super().display()
# manager=Manager('Durga',101,'AI')
# manager.approve_leave()
# manager.display()
# employee=Employee('Shiva',202)
# employee.display()
# person=Person('Guru')
# person.display()
#---------------------------------------------------------
#8Design a system where a base class `Animal` has a method `speak()`, and subclasses `Dog` and `Cat` override it.	
# class Animal:
#     def speak(self):
#         print('The animal is speaking')
# class Dog(Animal):
#     def speak(self):
#         print('The Dog is barking')
# class Cat(Animal):
#     def speak(self):
#         print('The cat is crying')
# animal=Animal()
# animal.speak()
# dog=Dog()
# dog.speak()
# cat=Cat()
# cat.speak()
#-------------------------------------------------------
#9. Simulate multiple inheritance where `FlyingCar` inherits from both `Car` and `defAirplane`.
#  Handle potential conflicts in the `move()` method.
# class Car:
#     def move(self):
#         print('The car is moving on the road')
#         super().move()
# class Airplane:
#     def move(self):
#         print('The Airplane is flying in the sky')
# class FlyingCar(Car,Airplane):
#     def move(self):
#          super().move()
# fc=FlyingCar()
# fc.move()
#-----------------------------------------------------------------
#10. Build a `SmartPhone` class inheriting from `MobileDevice`, which in turn inherits from `Electronics`.
#  Demonstrate method overriding and attribute reuse.
# class Electronics:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#     def display(self):
#         print(f'Brand:{self.brand} & Model:{self.model}')
# class MobileDevice(Electronics):
#     def __init__(self,brand,model):
#         super().__init__(brand,model)
#     def display(self):
#         super().display()
# class SmartPhone(MobileDevice):
#     def __init__(self, brand, model):
#         super().__init__(brand, model)
#     def display(self):
#         super().display()
# sp=SmartPhone('infinix',30)
# sp.display()
# mb=MobileDevice('Iphone',123)
# sp.display()
# el=Electronics('croma','grinder')
# el.display()
#------------------------------------------------------------------
#	11. Create a class `Logger` with a method `log(message)`. 
# Implement method overloading to log different message types (`error`, `warning`, `info`).
# class Logger:
#     def log(self,message):
#         if message == 'error':
#             print('You got an error')
#         elif message == 'warning':
#             print('You have a message')
#         else:
#             print('You have some info ')
# l1=Logger()
# l1.log('error')
# l1.log('warning')
# l1.log('info')
#-------------------------------------------------------------------------------------
#12. Write a `Payment` class with a method `process_payment()`. Implement subclasses `CreditCardPayment`, `PayPalPayment`, and 
# `BitcoinPayment` that override the method differently.
# class Payment:
#     def process_payment(self):
#         print('Welcome to payment process')
# class CreditCardPayment(Payment):
#     def process_payment(self):
#         print("Your payment was done with credit card")
# class PayPalPayment(Payment):
#     def process_payment(self):
#         print('Your payment was done through paypal gateway')
# class BitcoinPayment(Payment):
#     def process_payment(self):
#         print('Your payment was done by bitcoin')
# def func(obj):
#     obj.process_payment()
# cc=CreditCardPayment()
# func(cc)
# pp=PayPalPayment()
# func(pp)
# bit=BitcoinPayment()
# func(bit)
#------------------------------------------------------------
#13. Develop a `Shape` class with a method `area()`.
#  Implement `Square` and `Triangle` classes that provide specific implementations for `area()`.

# class Area:
#     def area(self):
#         print("Calculation of Area")
# class Sqaure(Area):
#     def __init__(self,side ):
#         self.side=side
#     def area(self):
#         super().area()
#         print(f'The area will be {self.side*self.side}')
# class Triangle(Area):
#     def __init__(self,length,breadth ):
#         self.length=length
#         self.breadth=breadth
#     def area(self):
#         super().area()
#         print(f'The area will be {self.length*self.breadth}')

# sq=Sqaure(4)
# sq.area()
# tr=Triangle(4,5)
# tr.area()
#==================================================================
#14.Implement method overriding for a `Notification` class where `send()` is overridden in
#  `EmailNotification` and `SMSNotification`.

# class Notification:
#     def send():
#         print('You sent a Notification')
# class EmailNotification(Notification):
#     def send(self):
#         print('You sent an Email Notification')
# class SMSNotification(Notification):
#     def send(self):
#         print('You sent a SMS Notification')
# em=EmailNotification()
# em.send()
# sms=SMSNotification()
# sms.send()
#=-------------------------------------------------------
#Abstract classes
#16. Create an interface `IShape` with an abstract method `calculate_area()`. Implement it in `Rectangle` and `Circle` classes.
# from abc import ABC,abstractmethod
# class IShape(ABC):
#     @abstractmethod
#     def calculate_area():
#         pass
# class Rectangle(IShape):
#     def calculate_area(self,length,breadth):
#         print(f'The area of the rectangle is {length*breadth}')
# class Circle(IShape):
#     def calculate_area(self,radius):
#         print(f'The area of the circle is {2*3.14*radius}')
# rect=Rectangle()
# rect.calculate_area(10,20)
# circ=Circle()
# circ.calculate_area(1)
#----------------------------------------------------------------------
#17. Define an abstract class `IDatabaseOperations` with methods `insert()`, `update()`, and `delete()`.
#  Implement this in `SQLDatabase` and `NoSQLDatabase`.
# from abc import ABC,abstractmethod
# class IDatabaseOperations(ABC):
#     @abstractmethod
#     def insert():
#         pass
#     @abstractmethod
#     def update():
#         pass
#     @abstractmethod
#     def delete():
#         pass
# class SQLDatabase(IDatabaseOperations):
#     def __init__(self):
#         self.data={}
#     def insert(self,id,name):
#         self.data[id]=name
#     def update(self,id,name):
#         self.data[id]=name
#     def delete(self,id):
#         del self.data[id]
#     def display(self):
#         print(self.data)
# class NOSQLDatabase(IDatabaseOperations):
#     def __init__(self):
#         self.data={}
#     def insert(self,id,name):
#         self.data[id]=name
#     def update(self,id,name):
#         self.data[id]=name
#     def delete(self,id):
#         del self.data[id]
#     def display(self):
#         print(self.data)
# sql=SQLDatabase()
# sql.insert(102,'shiva')
# sql.insert(103,'surya')
# sql.update(103,'narayana')
# sql.delete(102)
# sql.display()
# nsql=NOSQLDatabase()
# nsql.insert(102,'shiva')
# nsql.insert(103,'surya')
# nsql.update(103,'narayana')
# nsql.delete(102)
# nsql.display()
#-----------------------------------------------------------------------
#18. Implement an abstract class `ICalculator` with methods `add()`, `subtract()`, `multiply()`, and `divide()`.
#  Create a `BasicCalculator` class that implements these methods.
# from abc import ABC,abstractmethod
# class ICalculator(ABC):
#     @abstractmethod
#     def add():
#         pass
#     @abstractmethod
#     def subtract():
#         pass
#     @abstractmethod
#     def multiply():
#         pass
#     @abstractmethod
#     def divide():
#         pass
# class BasicCalculator(ICalculator):
#     def add(self,a,b):
#         print(f'Add: {a+b}')
#     def subtract(self,a,b):
#         print(f'Subtract: {a-b}')
#     def multiply(self,a,b):
#         print(f'Multiply: {a*b}')
#     def divide(self,a,b):
#         print(f'Division: {a/b}')
# bc=BasicCalculator()
# bc.add(10,20)
# bc.subtract(20,11)
# bc.multiply(20,40)
# bc.divide(40,20)
#----------------------------------------------------------------------------------
 #19.Develop an interface `IVehicle` with abstract methods `start_engine()` and `stop_engine()`. 
 # Implement it in `Car`, `Bike`, and `Truck` classes.

# from abc import ABC,abstractmethod
# class IVehicle(ABC):
#     @abstractmethod
#     def start_engine():
#         pass
#     def stop_engine():
#         pass
# class Car(IVehicle):
#     def start_engine(self):
#         print("The car engine is running")
#     def stop_engine(self):
#         print('The car engine has been stopped')
# class Bike(IVehicle):
#     def start_engine(self):
#         print("The Bike engine is running")
#     def stop_engine(self):
#         print('The Bike engine has been stopped')
# class Truck(IVehicle):
#     def start_engine(self):
#         print("The Truck engine is running")
#     def stop_engine(self):
#         print('The Truck engine has been stopped')
# car=Car()
# car.start_engine()
# bike=Bike()
# bike.start_engine()
# truck=Truck()
# truck.start_engine()
# car.stop_engine()
# bike.stop_engine()
# truck.stop_engine()
#-------------------------------------------------------
# 20.Write a scenario where a `UserAuthentication` interface contains `login()` and `logout()` methods,
#  and it is implemented by `GoogleAuth` and `FacebookAuth` classes.

# from abc import ABC,abstractmethod
# class UserAuthentication(ABC):
#     @abstractmethod
#     def login():
#         pass
#     @abstractmethod
#     def logout():
#         pass
# class GoogleAuth(UserAuthentication):
#     def login(self):
#         print("Google Login is successful")
#     def logout(self):
#         print('Google Logout is successful')
# class FacebookAuth(UserAuthentication):
#     def login(self):
#         print("Facebook Login is successful")
#     def logout(self):
#         print('Facebook Logout is successful')
# google=GoogleAuth()
# google.login()
# facebook=FacebookAuth()
# facebook.logout()
# google.logout()
# facebook.logout()