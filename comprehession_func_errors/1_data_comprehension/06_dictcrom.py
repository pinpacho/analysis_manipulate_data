import random

countries = ['col','mex','bol']
population = {}
for country in countries:
    population[country]=random.randint(1,100)

print(population)

population_v2={country:random.randint(1,100) for country in countries}
print(population_v2)


result = {pais : population3 for (pais, population3) in population_v2.items() if population3 > 20}
print(result)


text = 'Hola ,soy Julian'

unique = {c : c.upper() for c in text if c in 'aeiou'}
print(unique)