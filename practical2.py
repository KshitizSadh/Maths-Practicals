# Genrate the matrix into echelon form and find its rank
#using numpy

#Taking input of Matrix From user (User Define Matric Input)
#NR: Number of rows
#NC: Number of colums
import numpy as np
NR = int(input("Enter the number of rows"))
NC = int(input("Enter the number of colums"))

print("Enter the enteries in a single line (seprated by space): ")

#user input of entries in a
#single line seprated by space
entries =list(map(list,input().split()))

#For Printing the matrix
matrix = np.array(entries).reshape(NR,NC)
print("Matrix X is as follows:",'\n',matrix)

#For Finding the Rank of a matrix
print("the rank of a Matrix is:",np.linalg.matrix_rank(matrix))

         
