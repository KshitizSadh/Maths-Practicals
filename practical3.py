#Practical 3: FIND, DETERMINAT , ADJOINT AND INVERSE OF A MATRIX. #USING NUMPY
#Taking Input of Matrix From user (user define matrix Input)
import numpy as np
NR = ("Enter the number of Rows")
NC = ("Enter the number of colums")
print("Enter the entries in a single line (seprated by space): ")

#user input of entries in a
#single line aeprated by space
entries = list (map(int, input().split()))

#For printing the matrix
A = np.array(entries).reshape(NR,NC)
print("matrix X is as follows:",'\n', A)

A_Inverse = np.linalg.inv(A)
Transpose_of_A_Inverse = np.transpose(A_Inverse)
Determinant_of_A = np.linalg.det(A)
Cofactor_of_A = np.dot(Transpose_of_A_Inverse,Determinant_of_A)

#For finding the cofactor of a amtrix
print("the Cofactor of a matrix is:",'\n',Cofactor_of_A)

#for Finding the Determinat of a matrix
print("the Determinant of a matrix is:",'\n',Determinant_of_A)

#For Finding the adjoint of a matrix
Adjoint_of_A = np.transpose(Cofactor_of_A)
print("The Adjoint of a matrix is:",'\n',Adjoint_of_A)
                        
                
