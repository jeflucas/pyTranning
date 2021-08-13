# Strings in python are surronded by either single or double quotation marks.

name = 'Jeff'
age = 30

# Concatenate

#print('Hello, my name is ' + name + ' and I am ' + str(age) + ' years old!')

# String Formatting

## Arguments by position
#print('My name is {name} and I am {age}'.format(name = name, age = age))

## F-String (version 3.6+)
#print(f'Hello, my name is {name} and I am {age}')

# String Methods

s = 'hello world'

## Capitalize string
print(s.capitalize())

## Make all uppercase

print(s.upper())

## Make all lower

print(s.lower())

## Swap case

print(s.swapcase()) 

## Get length

print(len(s))

## Replace

print(s.replace('world', 'Jeff'))

## Count

sub = 'h'
print(s.count(sub))

## Starts with
print(s.startswith('hello'))

## Ends with
print(s.endswith(sub))

## Split into a list
print(s.split())

## Find position

print(s.find(' '))

## Is all alphanumerich

print(s.isalnum())

## is all alphabetich

print(s.isalpha())

## is all numeric

print(s.isnumeric())