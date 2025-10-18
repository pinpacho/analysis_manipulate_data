set_countries = {'col','mex','bol'}


#Tamaño
size = len(set_countries)
print(size)

#Objeto en el conjunto
print('col' in set_countries)
print('pe' in set_countries)

#add

set_countries.add('pe')
print(set_countries)
set_countries.add('pe')
print(set_countries)

#update

set_countries.update({'ar','ecua','pe'})
print(set_countries)

#remove
set_countries.remove('pe')
print(set_countries)
#set_countries.remove('arg')
set_countries.discard('arg')
print(set_countries)

#Clear
set_countries.clear()
print(set_countries)