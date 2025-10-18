number = []

for element in range(1,11):
    number.append(element)


print(number)


#Another way
number_2=[element *2 for element in range(1,11)]
print(number_2)



numbers=[]
for i in range(1,11):
    if i % 2 == 0:
        numbers.append(i**2)

print(numbers)

numbers_v2=[i ** 2 for i in range(1,11) if i%2 ==0]
print(numbers_v2)