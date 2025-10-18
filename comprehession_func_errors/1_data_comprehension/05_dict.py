import random

dict = {}
for i in range(1,11):
    dict[i]=i**2

print(dict)

dict2 = {i:i **2 for i in range (1,11)}
print(dict2)


countries = ['col','mex','bol']
population = {}
for country in countries:
    population[country]=random.randint(1,100)

print(population)

population_v2={country:random.randint(1,100) for country in countries}
print(population_v2)


names=['Juan','Nico','Sandra']
ages=[12,54,46]

print(list(zip(names,ages)))

peoples_dict ={ name : age for (name,age )in zip(names,ages)}
print(peoples_dict)