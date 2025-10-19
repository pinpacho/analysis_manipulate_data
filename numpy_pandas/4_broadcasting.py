import numpy as np 

prices = np.array([100,200,300])


discounts = np.array([0.9])

discounts_prices = prices * discounts
print(discounts_prices)


#Array resta

prices = np.random.randint(100,500,size=(3,3))
discounts = np.array([10,20,30])
discounted_prices = prices - discounts
print(prices)
print(discounts)
print(discounted_prices)#Resta cada fila

array = np.array([1,2,3,4,5])
print(np.all(array > 4))   #False si todos cumplen la condicion
print(np.any(array > 4 ))#True si al menos uno cumple la condicion



array_a = np.array([1,2,3])
array_b = np.array([4,5,6])
concatened = np.concatenate((array_a,array_b))
print(concatened)
concante2=np.concatenate((array_a,array_a))#Concatena el mismo array
print(concante2)


satecved=np.vstack((array_a,array_b))#Apila verticalmente
print(satecved)
sateched=np.hstack((array_a,array_b))#Apila horizontalmente
print(sateched)


array_c = np.arange(1,10)
split=np.split(array_c,3)
print(split)
print(array_c)