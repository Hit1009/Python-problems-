#D1Write a program to check whether a number is odd or even
n=int(input("Enter a number:"))
if n%2==0:
    print(n,"is an even number")
else:
    print(n,"is an odd number")
    
print("")

#D2Write a program in python to find the biggest of two numbers.
n1=float(input("Enter 1st number:"))
n2=float(input("Enter 2nd number:"))
if n1>n2:
    print(n1,"is largest")
else:
    print(n2,"is largest")
    
print("")

#D3Write a program to convert a character from lower case to uppercase and vice versa
a=input("Enter a character:")
if a.upper()!=a:
    print("uppercase =",a.upper())
else:
    print("lowercase =",a.lower())

print("")

#D4Write a program in python to find whether a number is divisible by both 5 and 7 .
n=int(input("Enter a number:"))
if n%5==0 and n%7==0:
    print(n,"is divisible by 5 and 7")
else:
    print(n,"is NOT divisible by 5 and 7")

print("")

#D5 Write a program to find the input year is leap year or not.
y=int(input("Enter a year:"))
if y%4!=0:
    print(y,"is not a leap year")
else:
    if y%100!=0:
        print(y,"is a leap year")
    else:
        if y%400!=0:
            print(y,"is not a leap year")
        else:
            print(y,"is a leap year")
             
print('')

#D6Write a program in python to input three sides of a triangle and check whether the triangle is equilateral, isosceles or scalene
a=float(input("side1="))
b=float(input("side2="))
c=float(input("side3="))
if a!=b and b!=c and c!=a:
    print("Scalene triangle")
else:
    if a==b and b==c and c==a:
        print("Equilateral triangle")
    else:
        print("Isosceles triangle")
        
print("")   
   
#D7Write a program in python to input three sides of a triangle and check whether it is right angled one
a=float(input("side1="))
b=float(input("side2="))
c=float(input("side3="))
if a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==a**2+b**2:
    print("Right angled triangle")
else:
    print("Not a right angled triangle")
    
print("")

#D8 Read a number, check if it is positive, negative or zero. Increment the number if it is positive, decrement if it is negative.
n=float(input("Enter a number:"))
if n<0:
    print(n,"is negative","decrement=",n-1)
elif n==0:
    print(n,"is zero")
elif n>0:
    print(n,"is positive, increment=",n+1)
  
print("")  

#D9Create a simple calculator.
print("1.Addition 2.Subtraction 3.Multiplication 4.Division")
a=int(input("Enter 1,2,3 or 4:"))
n1=float(input("Enter 1st number n1:"))
n2=float(input("Enter 2nd number n2:"))
if a==1:
    sum=n1+n2
    print("n1 + n2 =",sum)
elif a==2:
    diff=n1-n2
    print("n1 - n2 =",diff)
elif a==3:
    p=n1*n2
    print("n1 x n2 =",p)
elif a==4:
    d=n1/n2
    print("n1/n2 =",d)
    
print("")   
 
#D10Estimate the Grade based on the marks obtained by a student.
print("Enter Marks Obtained in 5 Subjects: ")
markOne = int(input())
markTwo = int(input())
markThree = int(input())
markFour = int(input())
markFive = int(input())

tot = markOne+markTwo+markThree+markFour+markFive
avg = tot/5

if avg>=91 and avg<=100:
    print("Your Grade is A1")
elif avg>=81 and avg<91:
    print("Your Grade is A2")
elif avg>=71 and avg<81:
    print("Your Grade is B1")
elif avg>=61 and avg<71:
    print("Your Grade is B2")
elif avg>=51 and avg<61:
    print("Your Grade is C1")
elif avg>=41 and avg<51:
    print("Your Grade is C2")
elif avg>=33 and avg<41:
    print("Your Grade is D")
elif avg>=21 and avg<33:
    print("Your Grade is E1")
elif avg>=0 and avg<21:
    print("Your Grade is E2")
else:
    print("Invalid Input!")

print("")

#D11 Obtain a character, check if it is lower case, uppercase or digit.
n = input("Enter a character:  ")
if n <=str(9) and len(n)==1:
    print(n,"is digit")
elif len(n)!=1:
    print("Error, enter 1 digit character")
else:
    if n==n.upper():
        print(n,'is uppercase')
    else:
        print(n,'is lowercase')
        
print("")

#D12Find the largest of 3 numbers.
n1=float(input("Enter 1st number n1:"))
n2=float(input("Enter 2nd number n2:"))
n3=float(input("Enter 3rd number n3:"))
if n1>n2 and n1>n3:
    print(n1,"is largest")
elif n2>n1 and n2>n3:
    print(n2,"is largest")
elif n3>n1 and n3>n2:
    print(n3,"is largest")
 
print("")

#D13Obtain a input from the user and display the corresponding data types primitive and compound data type
a=input("Enter data:")
if a==int(a) or a==float(a) or a==str(a):
    print(a,"is a primitive data type")
else:
    print(a,"is a compound data type")
    