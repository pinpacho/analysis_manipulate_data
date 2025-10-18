set_a = {'col','mex','ec'}
set_b = {'pe','arg','col'}

#Union
set_c = set_a.union(set_b)
print(set_c)
print(set_a | set_b)

#Interseccion
set_c = set_a.intersection(set_b)
print(set_c)
print(set_a & set_b)

#Resta
set_c = set_a.difference(set_b)
print(set_c)
print(set_a - set_b)

#Diferencia simetrica
set_c = set_a.symmetric_difference(set_b)
print(set_c)
print(set_a ^ set_b)