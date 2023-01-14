#A1 Write a program in python to add two numbers and print the result.
n1=float(input("Enter 1st number:"))
n2=float(input("Enter 2nd number:"))
sum=n1+n2
print(n1,"+",n2,"=",sum)
print("")
#A2 Write a program in python to find the area of a triangle.
base=float(input("Enter base length of the triangle:"))
height=float(input("Enter height of the triangle"))
area=(1/2)*base*height
print("area of triangle=",area)

print("")

#A3 Write a program in python to find square root of a number.
n=float(input())
sqrt=n**(1/2)
print("square root=",sqrt)

print("")

#A4Write a program in python to solve a quadratic equation
a=int(input("coefficient of x^2:="))
b=int(input("coefficient of x="))
c=int(input("constant="))
d=((b**2)-4*a*c)**(1/2)
x1=(-b+d)/2
x2=(-b-d)/2
print("x=",x1,x2)

print("")

#A5Write a program in python to convert Fahrenheit to Celsius.
tempf=float(input("Enter temperature in fahrenheit:"))
tempc=(tempf-32)*(5/9)
print(tempf,"°F","=",tempc,"°C")

print("")

#A6Write a program in python to find quotient and reminder after division
dvdt=int(input("Enter the divident:"))
dvsr=int(input("Enter the divisor:"))
qnt=dvdt//dvsr
rem=dvdt%dvsr
print("Quotient=",qnt,"","remainder=",rem)

print("")

#A7Write a program in python to swap two numbers using tuple assignment.
n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))
print("n1=",n1,"n2=",n2)
tup=(n1, n2)
n1,n2=tup[-1],tup[0]
print("swapped numbers:","n1=",n1,"n2=",n2)

print("")

#A8write a program in python to find the average of three marks.
m1=int(input("Enter 1st marks:"))
m2=int(input("Enter 2nd marks:"))
m3=int(input("Enter 3rd marks:"))
avg=(m1+m2+m3)/3
print("Average marks=",avg)

print("")

#A9Write a program in python to calculate simple interest.
p=int(input("Enter the principle amount:"))
t=int(input("Enter time duration:"))
r=int(input("Enter rate of interest:"))
s=(p*t*r)/100
print("simple interest=",s)

print("")

#A10Write a program in python to calculate the net pay given basic pay, hra, da and deductions.
days=float(input("Enter No Days Present:"))
wages=float(input("Enter wages per Day:"))
basic=wages*days;
HRA=basic*0.1;
DA=basic*0.05;
PF=basic*0.12;  
netsalary=basic+HRA+DA-PF;
print("\nBasic:%lf \nHRA:%lf \nDA:%lf \nPF:%lf \nNet Salary:%lf" %(basic,HRA,DA,PF,netsalary));
