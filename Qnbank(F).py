#F1Write a Python program to construct the following pattern, using a nested for loop
#a
for i in range(0,5):
    for j in range(i):
        print("*",end=" ") 
    print()
    
for i in range(5,0,-1):
    for j in range(i):
       print("*",end=" ") 
    print()
print() 
#b
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ") 
    print()
print()
#c
n=7
for i in range(n+1):
      for j in range(n-i):
         print(' ', end='')

      C = 1
      for j in range(1, i+1):
         print(C, ' ', sep='', end='')
         C = C * (i - j) // j
      print()
      
print()

#F2 Write a Python program that accepts a word from the user and reverse it. 
a='Hellow'
l=[]
for i in range(len(a)):
    l.append(a[i])    
for i in range(len(a)):
    l[i]=a[-1-i]
b=""
for i in l:
    b+=i
print(b)

print()

#F3 Write a Python program to count the number of even and odd numbers from a series of numbers. 
l=[1,2,3,4,5,6,7,8,9,10]
evensum=0
oddsum=0
for i in l:
    if i%2==0:
        evensum+=i
    elif i%2==1:
        oddsum+=i
print('evensum=',evensum)
print("oddsum=",oddsum)

print()

#F4. Write a Python program that prints each item and its corresponding type from the following list. 
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12],
{"class":'V', "section":'A'}] 
for i in datalist:
    print(i,type(i))

print()

#F5 Write a Python program that prints all the numbers from 0 to 6 except 3 and 6. Note : Use 'continue' statement. 

for i in range(0,6):
  if i==3 or i==6:
      continue
  print(i) 
  
print()

#F6 Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz". 
for i in range(1,51):
    if i%3==0 and i%5!=0:
        print("Fizz")
    elif i%5==0 and i%3!=0:
        print("Buzz")
    elif i%5==0 and i%3==0:
         print("FizzBuzz")
    else:
        print(i)

print()

#F7 Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number. The numbers obtained should be printed in a comma-separated sequence
Even_digits_nos=[]
for i in range(0,401):
    t=str(i)
    if len(t)==1:
        if int(t[0])%2==0:
            Even_digits_nos.append(i)
    if len(t)==2:
        if int(t[0])%2==0 and int(t[1])%2==0:
            Even_digits_nos.append(i)
    if len(t)==3:
        if int(t[0])%2==0 and int(t[1])%2==0 and int(t[2])%2==0:
              Even_digits_nos.append(i)
print("The numbers from 0 to 400 whose each digit is even are:",Even_digits_nos)   

print()

#F8 Write a Python program to create the multiplication table (from 1 to 10) of a number. 
a=6
for i in range(1,11):
  print(a,"×",i,"=",a*i)

print()

#F9(a). Find the sum of series:a. 1 + 1/2 + 1/3 + ….. + 1/N 
n=5 #specifing number of terms in series
sum=0
for i in range(1,n+1):
  sum=sum+1/int(i)
print(sum)

print()

#F9(b). Find the sum of series 1 + x^2/2 + x^3/3 + … x^n/n
n=5 #specifing number of terms in series
x=2 #specifing the value of x
sum=1
for i in range(2,n+1):
  sum+=x**i/i
print(sum)

print()

#F10. Classify the given number is prime or composite number. 
n=11 #test case
for i in range(2,n):
    if n%i==0:
        print(n,"is a composite number")
        break
    else:
        print(n,"is a prime number")
        break