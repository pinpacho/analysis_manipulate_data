import numpy as np 


#Escalar dimension 0
escalar = np.array(42)
print(escalar)
print("Tipo de dato del escalar:", escalar.dtype)
print("Dimensiones del escalar:", escalar.ndim)

#Vector

vector = np.array([312,412,431,273])
print(vector)
print("Dimensiones del vector:", vector.ndim)
print(type(vector))

#Matriz 2D
matriz_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(matriz_2d)
print("Dimensiones de la matriz 2D:", matriz_2d.ndim)
print(type(matriz_2d))

#Tensor 3D
tensor_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(tensor_3d)
print("Dimensiones del tensor 3D:", tensor_3d.ndim)
print(type(tensor_3d))


#Arange  Crea una secuencia de números en un array

array_arrange = np.arange(10)
print("Array con arange:", array_arrange)


#Identidad eye Crea una matriz identidad
matriz_identidad = np.eye(4)
print("Matriz identidad:\n", matriz_identidad)

#Diagonal Crea una matriz diagonal a partir de un array
array_diagonal = np.array([1, 2, 3, 4])
matriz_diagonal = np.diag(array_diagonal)
print("Matriz diagonal:\n", matriz_diagonal)

#Random Crea un array con valores aleatorios
array_random = np.random.rand(3, 3)
print("Array con valores aleatorios:\n", array_random)