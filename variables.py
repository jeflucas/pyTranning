# A variable is a container for a value, which can be of various types

'''
This is a multiline comment
or docstring (used to define a functions propose)
can be single os double quotes
'''

"""
Variable rules:
- Variable names are case sensitive (name, Name and NAME are different variables)
- Must star with a letter or an undesrscore
- Can have numbers but can not star with a number
"""

#x = 1           #int
#y = 2.5         #float
#name = 'Jeff'   #string
#is_cool = True  #boolean

# Multiple assignment

x, y, name, is_cool = (1, 2.5, 'Jeff', True)

# Basic math

a = x + y

# casting

x = str(x)
y = int(y)
z = float(y)

print(type(z), z)