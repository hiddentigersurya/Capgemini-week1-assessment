# ***********1. ATM Simulation***********
# def check_balance():
#     print(f"Your account balance is: {amount} \n")
# def deposit():
#     cash=int(input("Enter the amount to deposit: \t"))
#     print("You have successfully deposited the amount \n")
#     return cash
# def withdraw():
#     cash=int(input("Enter the amount to withdraw: \t"))
#     if(cash>amount):
#         print("Sorry, you don't have suffient funds in your account \n")
#         return 0
#     else:
#         print("Please take your cash \n")
#         return cash
# print("Welcome")
# amount=10000
# while(True):
#     print("1.check balance \n2.cash deposit \n3. cash withdrawal \n4.exit")
#     option=int(input('Enter the option: \t'))
#     if(option==1):
#         check_balance()
#     elif(option==2):
#         a=deposit()
#         amount+=a
#     elif(option==3):
#         am=withdraw()
#         amount-=am
#     else:
#         print("Thank you, you can exit now")
#         break
# -------------------------------------------------------------------------------------------
# ***********4. Temperature Conversion Tool**********
# def celius(degree):
#     k=degree+273.15
#     print(f'{k} kelvin')
#     f=int((9*degree)/5)+32
#     print(f'{f} fahrenheit')
# def kelvin(degree):
#     f=int((9*(degree-273.15))/5)+32
#     print(f'{f} fahrenheit')
#     c=degree-273.15
#     print(f'{c} celsius')
# def fahren(degree):
#     c=int((5*(degree-32))/9)
#     print(f'{c} celsius')
#     k=int((5*(degree-32))/9)+273.15
#     print(f'{k} kelvin')
# degree=float(input('Enter numeric value of temperature:  '))
# print('1.Celsius\n2.Kelvin\n3.Fahrenheit\n')
# option=int(input('Enter the option for input temperature type: \t'))
# if(option==1):
#     celius(degree)
# elif(option==2):
#     kelvin(degree)
# elif(option==3):
#     fahren(degree)
# else:
#     print('Invalid Option')
# ------------------------------------------------------------------------------------------------
# *****4.Number Guessing Game********
# import random
# random_number=random.randint(1,100)
# print("Welcome to the Number Guessing Game\n")
# attempts=0
# print("Let's go, Guess the number\n")
# while(True):
#     number=int(input('Enter the number :'))
#     if(number>random_number):
#         print("It's too high")
#     elif(number==random_number):
#         print('You won the Game')
#         break
#     else:
#         print("It's too low")
#-------------------------------------------------------------------------------------------

#*********4.Student Grading System**********
# name=input("Enter the student name: ")
# print("Enter the subject marks with spaces\n")
# marks=list(map(int,input().split()))
# total=sum(marks)
# percentage=(total/500)*100
# Grade=''
# if(percentage>90):
#     Grade='A'
# elif(percentage>80):
#     Grade='B'
# elif(percentage>60):
#     Grade='C'
# else:
#     Grade='Fail'
# print(f'Total Marks= {total}')
# print(f'Percentage is {percentage}%')
# print(f'Grade : {Grade}')
#------------------------------------------------------------------------
#**************5.shopping cart*****************
# lists=[]
# def add():
#     name=input("Enter the item name: ")
#     price=int(input('Enter the price: '))
#     lists.append([name,price]) 
# def view():
#     for i in lists:
#         print(i)
# def total():
#     ans=0
#     for i in lists:
#         ans+=i[1]
#     return ans
# print("**Welcome to shopping**")
# while True:
#     option=int(input("1.Add Item\n2.View Cart Items\n3.Total Price\n4.Exit\nEnter the option: "))
#     if(option==1):
#         add()
#     elif(option==2):
#         view()
#     elif(option==3):
#         print(total())
#     else:
#         print("Thank you for shopping")
#         break
#---------------------------------------------------------------------------------------------------
#*********************6.prime numbers in range*******************
# def prime(n):
#     if(n<=1):
#         return False
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True
# start=int(input("Enter the starting number: \t"))
# end=int(input("Enter the ending number: \t"))
# if(start>=end):
#     print("Starting number should be less than ending number")
# else:
#     for i in range(start,end+1):
#         if(prime(i)):
#             print(i,end=' ')
#-------------------------------------------------------------------------------

#************7.loan eligibility********************
# salary=int(input('Enter your salary: '))
# age=int(input("Enter your age: "))
# credit_score=int(input("Enter your credit score: "))
# if(age<18):
#     print("Loan Rejected: You are minor")
# elif(salary<200000):
#     print("Loan Rejected: Salary should be more than 2 Lakhs")
# elif(credit_score<500):
#     print("Loan Rejected: Your Credit score is too low")
# else:
#     print("Loan Approved")
#--------------------------------------------------------------------------------

#***********8.Multiplication*****************************
# number=int(input("Enter the number: "))
# rang=int(input("Enter the range: "))
# for i in range(1,rang+1):
#     print(f'{number} * {i} = {number*i}')
#----------------------------------------------------------------------------------

# **************9.string analyzer***********************
# vowels=['a','e','i','o','u']
# s=input("Enter the string:\n")
# s=s.lower()
# no_of_consonants=0
# no_of_vowels=0
# no_of_digits=0
# no_of_special_characters=0
# for i in s:
#     if i in vowels:
#         no_of_vowels+=1
#     elif i.isalpha():
#         no_of_consonants+=1
#     elif i.isdigit():
#         no_of_digits+=1
#     else:
#         no_of_special_characters+=1
# print(f'No.of Consonants: {no_of_consonants}')
# print(f'No.of Vowels: {no_of_vowels}')
# print(f'No.of Digits: {no_of_digits}')
# print(f'No.of Special Characters: {no_of_special_characters}')
#-------------------------------------------------------------------------------------

#***********************10.Bill splitter*********************************
# amount=int(input("Enter the total bill amount: "))
# n=int(input("Enter no.of people: "))
# tip=float(input("Enter tip percentage, Otherwise enter 0: "))
# amount+=((tip/100)*amount)
# each=float(amount/n)
# print(f"Each person should pay {each} rupees.")
#-------------------------------------------------------------------------------------

#*************************11.password strength checker*******************************
# password=input("Enter the password: ")
# n=len(password)
# upp=0
# low=0
# digi=0
# special=0
# if(n<8):
#     print("Password is weak")
# else:
#     for i in password:
#         if i.isalpha():
#             if i.lower()==i:
#                 low+=1
#             else:
#                 upp+=1
#         elif(i.isdigit()):
#             digi+=1
#         else:
#             special+=1
#     if(upp and low and special and digi):
#         print("Password is Strong")
#     else:
#         print("Password is weak")
#-------------------------------------------------------------------------------------

#*********************12.pattern Generator************************
# n=int(input("Enter the number:"))
# for i in range(1,n+1):
#     print('*'*i)
# a=int(input("Enter 1 to view reverse pattern: "))
# if(a):
#     for i in range(n):
#         print('*'*(n-i))
#-------------------------------------------------------------------------------------

#************************13.palindrome checker***************************
# q=1
# while q:
#     s=input("Enter the input:")
#     if(s==s[::-1]):
#         print("Yes, it is a palindrome")
#     else:
#         print("No, it is not a palindrome")
#     print('Enter 0 to discontinue, otherwise enter any number')
#     q=int(input())
#-------------------------------------------------------------------------------------

#************************14.factorial calculator*************************
# number=int(input("Enter the number: "))
# fact=1
# if(number<0):
#     print("Enter positive numbers")
# else:
#     for i in range(1,number+1):
#         fact*=i
#     print(fact)
#-------------------------------------------------------------------------------------

#********************15.leap year checker***************************
# q=1
# while q:
#     year=int(input("Enter the year: "))
#     if(year%4==0):
#         if(year%100==0 and year%400!=0):
#             print("It is not leap year")
#         else:
#             print("It is a leap year")
#     else:
#         print("It is not a leap year")
#     q=int(input("Enter 0 to exit, otherwise print any number"))
#-------------------------------------------------------------------------------------

#*************16.odd & even separator***********************
# arr=list(map(int,input("Enter the numbers with spaces: ").split()))
# odd=[]
# even=[]
# for i in arr:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(f'odd numbers:{odd}')
# print(f'even numbers:{even}')
#-------------------------------------------------------------------------------------

#***************17.word counter**********************
# file={}
# sent=input("Enter the sentence: ").split()
# for i in sent:
#     if(i not in file):
#         file[i]=1
#     else:
#         file[i]+=1
# print(file)
#-------------------------------------------------------------------------------------

#**************18.BMI Calci************************
# weight=float(input("Enter your weight(kg):"))
# height=float(input("Enter your height(m):"))
# BMI=(weight/(height**2))
# print(f"Your BMI : {BMI}")
# if(BMI<18.5):
#     print("Underweight")
# elif(BMI<=25):
#     print("Normal")
# elif(BMI<=30):
#     print("Overweight")
# else:
#     print("Obese")
#-------------------------------------------------------------------------------------

#*************19.second largest number*******
# arr=list(map(int,input("Enter the numbers:").split()))
# s=set(arr)
# n=len(s)
# s=list(s)
# s.sort()
# if(n<=1):
#     print('No second largest')
# else:
#     print(s[n-2])
#-------------------------------------------------------------------------------------

#*******20.FizzBuzz*************
# for i in range(1,101):
#     if(i%3==0 and i%5==0):
#         print('FizzBuzz')
#     elif(i%3==0):
#         print('Fizz')
#     elif(i%5==0):
#         print('Buzz')
#     else:
#         print(i)
#-------------------------------------------------------------------------------------
