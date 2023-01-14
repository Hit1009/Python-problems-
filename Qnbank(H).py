#H1. Calculate factorial of a given number using recursive function. The base case should handle the negative integers by printing an error message and returns none to indicate that something went wrong. 
def fact(n):
  if n<0: #This will diaplay error message and return None for negative numbers
    print("Error, factorial is not defined for negative numbers!")
    return None #This line does not have any effect
  if n==1:
    return 1
  else: 
    factorial=n*fact(n-1)
    return factorial
print(fact(-5)) #test case for negative number 
print("factorial is",fact(5)) #test case for positive number

print()

#H2. Compute the sum of the digits of a given number using recursion. 
def dgts_sum(n):
    if n==0:
        return 0
    else:
        return(n%10+dgts_sum(int(n)//10))
n=222 #test case
print("sum of digits is",dgts_sum(n))

print()

#H3. Check whether a given number is prime or not using recursive function.
def primechk(n,i=2):
    if n==2:
        return "Prime"
    if n==0 or n==1:
        return "not prime"
    if n%i==0:
        return "Not prime"
    else:
        return "Prime"
    return (prime(n,i+1))
a=63 #test case
b=12 #test case
print(primechk(a))
print(primechk(b))

print()

#H4. Write a recursive function called gcd that takes parameters a and b and returns their greatest common divisor.
def gcd(a,b):
  if b==0:
    return a
  return gcd(b,a%b)
print(gcd(15,18)) #test case

print()

#H5. The Ackermann function
def A(m,n):
    if m==0:
        return n+1
    if m>0 and n==0:
        return(A(m-1,1))
    if m>0 and n>0:
        return(A(m-1,(A(m,n-1))))
print(A(2,2)) #test case 1
print(A(0,5)) #test case 2
print(A(2,0)) #test case 3

