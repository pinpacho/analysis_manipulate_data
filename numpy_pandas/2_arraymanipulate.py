import numpy as np  


array = np.array([[1,2,3],[4,5,6]])
print(array.ndim)#ndim Dimension del array
print(array.shape)#shape Forma del array
print(array.dtype)#Tipo del array

#np.uint8
z = np.array(3,dtype=np.uint8)
print(z)

#dtype='d' Convierte a flotante
double_array=np.array([1,2,3],dtype='d')
print(double_array)

#Convertir z a float
z = z.astype(np.float64)
print(z)

#Suma array
print(array)
sum = np.sum(array)
print(sum)

#Media
mean = np.mean(array)
print(mean)

#Desviacion estandar
std= np.std(array)
print(std)