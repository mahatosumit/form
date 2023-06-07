#print("Hello World")
# find sum of two numbers
'''a = int(input("Enter first number"))
b = int(input("Enter second number"))
sum = a + b
subtract = a - b
divide = a/b
product = a*b
print(sum)
print(subtract)
print(divide)
print(product)

# Find the odd or even number
num = int(input("Enter a number"))
if (num % 2) == 0:
    print("The given number is even" .format(num))
else:
    print("The given number is odd" .format(num))
# find greatest number among two numbers
a = int(input("Enter first number"))
b = int(input("Enter second number"))
if a>b :
    print("a is greater number" .format(a))
else:
    print("b is greater number" .format(b)) 

# Check the given number is prime.
num = int(input("Enter a number:"))
if num > 1:
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            print(num , "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else: 
    print(num ,"is not prime number") 
#chech whether the year is leap or not
year = int(input("Enter the year\n"))
if (year%4) == 0:
    print("The given year is leap")

else:
    print("The given year is not leap") 
#calculate sqroot of the given number
import math
num = int(input("Enter any number"))
sqroot = math.sqrt(num)
print(f"The square root of {num} is:" , sqroot) 
##calculate sqroot of the given number without using math function
num = int(input("Enter any number\n"))
sqroot = num * 0.5
print(f"The square root of {num} is:" , sqroot)'''
#find the area of triangle
'''base = int(input("Enter the base of triangle:\n"))
height = int(input ("Enter the height of triangle:\n"))
area = 1/2 * base*height
print("The area of triangle is:\n", area) 
#find the area of circle
radius = int(input("Enter the radius of a circle"))
area = 4*3.14*radius**2
print("The area of circle is:\n" ,area) 
#print calender 
import calendar
year = 2023
month = 1
print(calendar.month(year , month))
# to find today's date
from datetime import date
today = date.today()
print(f"Todays date:\n" , today)

#print current time and date
from datetime import datetime
now = datetime.now()
print("The current date and time is:\n" , now) '''


