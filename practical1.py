# Practical 1: create and transform vectors ad matrices (the transpose vector (matrix) conjugate
# transpose of a vector (matrix)) 
#Program to  transpose a matrix
#using numpy
#taking input of matrix From User (User Define matrix input ) 
#NR: Number of rows
#Nc: Number of colums
import numpy as np 
NR = int(input("Enter the number the of rows:"))
NC = int(input("Enter the number of colums:"))


print("Enter the entries in a single line (seprated by space): ")

#user input of entries in a
# single line seprated by space
enteries = list (map(int, input().split()))

#For printing the matrix
matrix = np.array(enteries).reshape(NR,NC)
print("Matrix X is as follows:",'\n', matrix)

# For transposing the matrix 
print("Transpose of matrix X is as follows:",'\n',np.transpose(matrix))
    
