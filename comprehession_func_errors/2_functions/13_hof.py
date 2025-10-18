#High Order Function

def increment(x):
    return x+1

def high_order_func(x,func):
    return x +func(x)

y = lambda x:x**2

#Increment
print(high_order_func(2,increment))

#Lambda
print(high_order_func(2,y))