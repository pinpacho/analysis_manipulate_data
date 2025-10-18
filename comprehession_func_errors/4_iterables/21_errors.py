# print(0 / 0)
# print(result)
print('Hola')

suma = lambda x,y: x + y
assert suma(2,2) ==4 #Verificar que la funcion esta bien

print('Hola 2')

age = 10
if age < 18:
  raise Exception('No se permiten menores de edad') #Lanzar tu propio error

print('Hola 2')