#K1.Write a function to create and return the r X c matrix with the user input. Write another function to print the sums of each row.
matrix = []
def mat(R,C):
    global matrix
    for i in range(R):          
        a =[]
        for j in range(C):      
             a.append(int(input()))
        matrix.append(a)          
    for i in range(R):
        for j in range(C):
            print(matrix[i][j], end = " ")
        print()
mat(3,3)
def rowsum():
  global matrix
  for i in matrix:
    rowsum=0
    for j in i:
      rowsum+=j
    print("rowsum=",rowsum)
rowsum()

print()

#K2.Find the transpose of a given matrix using list comprehension. 
m = [[1,2],[3,4],[5,6]]
for row in m :
    print(row)
rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
print("\n")
for row in rez:
    print(row)

print()

#K3.For two matrices A and B, compute A+B and A*B. Show your answer with and without list comprehension
#Add two matrix
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range(len(X)):
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

for r in result:
   print(r)
print()
result = [[X[i][j] + Y[i][j]  for j in range(len(X[0]))] for i in range(len(X))]
for r in result:
   print(r)
print()
#mulitply two matrix
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]
for i in range(len(X)):
   for j in range(len(Y[0])):
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)
print()
result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]

for r in result:
   print(r)