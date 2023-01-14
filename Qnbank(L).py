#L1. Write a user-defined function to print and store squares of numbers for the given range into a dictionary.
d=dict()
for x in range(2,5+1):
    d[x]=x**2
print(d)

print()

#L2. Write a function named reverseLookup that finds all of the keys in a dictionary that map to a specific value
def reverseLookup(data,value):
  keys=[]
  for key in data:
    if data[key]==value:
      keys.append(key)
  return keys
def main():
  FrEn={"le":"the", "la":"the", "livre":"book", "pomme":"apple"}
  print("The french word for ‘the’ =",reverseLookup(FrEn,'the'))
  print("The french word for ‘apple’ =",reverseLookup(FrEn,'apple'))
  print("The french word for ‘food’ =",reverseLookup(FrEn,'food'))
main()

print()

#L3.Create a new dictionary by combining two dictionaries whose key-value pairs are given.The new dictionary has to be created by adding values for common keys from the two dictionaries. 
A = {'A':100, 'B':200, 'C':300}
B = {'A':300, 'B':500, 'D':400}
c = {x: A.get(x, 0) + B.get(x, 0) for x in set(A).union(B)}
print(c)
