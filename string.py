# Strings in python are surronded by either single or double quotation marks.

name = 'Jeff'
age = 30

# Concatenate

#print('Hello, my name is ' + name + ' and I am ' + str(age) + ' years old!')

# String Formatting

## Arguments by position
#print('My name is {name} and I am {age}'.format(name = name, age = age))

## F-String (version 3.6+)
print(f'Hello, my name is {name} and I am {age}')