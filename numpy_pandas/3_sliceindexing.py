import numpy as np

array = np.array([10,20,30,40,50])
print(array[1])
print(array[-1])

print(array[-1:-7])

#Bool index saca true o false de un array
bool_index = array > 25
print(bool_index)
print(type(bool_index))


#Se puede acceder a los datos del array mediante una lista
index = [2,3,0]
print(array[index])


array2 = np.random.randint(1,10,size=(3,3))
print(array2)
print(array2[0,1])
print(array2[:2,:2])