import numpy as np

survey_responses = np.array(["bueno","malo","excelente",
                             "bueno","malo","bueno"])

print(np.unique(survey_responses))#Devuelve los valores unicos del array

unique_elements, counts = np.unique(survey_responses, return_counts=True)
print(unique_elements)#Elementos unicos
print(counts)#Cantidad de veces que se repite cada elemento


array_x = np.arange(10)
view_y = array_x[1:3]
print(array_x)
print(view_y)
array_x[1:3]= [10,11]
print(array_x)
print(view_y)#La vista cambia al cambiar el array original


array_x = np.arange(10)

copy_x= array_x[[1,2]].copy()
print(array_x)
print(copy_x)
array_x[1:3]=[10,11]
print(array_x)
print(copy_x)#La copia no cambia al cambiar el array original