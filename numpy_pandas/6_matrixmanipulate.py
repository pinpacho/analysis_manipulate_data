import numpy as np

#Transpuesta
matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
transposed = matrix.T
print("Original Matrix:")
print(matrix)
print("Transposed Matrix:")
print(transposed)


#Reshape
array = np.arange(1,13)
reshaped_array=array.reshape(3,4)#Cambiar la forma del array
print("Original Array:")
print(array)
print("Reshaped Array (3x4):")
print(reshaped_array)


#Reverse
array = np.arange(1,13)
reversed_array = array[::-1]#Invierte el array
print("Original Array:")
print(array)
print("Reversed Array:")
print(reversed_array)


#Flatten COnvierte un array multidimensional en un array unidimensional
matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
flattened_array= matrix.flatten()
print("Original Array:")
print(matrix)
print("Flattened Array:")
print(flattened_array)