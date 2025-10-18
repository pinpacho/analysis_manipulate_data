def increment(x):
    return x+1


y = lambda x: x+1
resultado= y(2)
print(increment(10))
print(resultado)


full_name = lambda name, last_name: f'Full name is {name.title()} {last_name.title()}'

text = full_name('nicolas', 'perez casas')
print(text)