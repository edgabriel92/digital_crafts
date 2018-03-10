# What happens? Does it work? Does it not work? Why? What could be changed to make it work?

print x
""" 
there is an NameError 
no it doesn't work
'x' isn't defined
we can define x with a value on the pervious line
"""

x = 4
y = 'y'
print x + y
"""
there is a TypeError
no it doesn't work
both operands should have the same type
we can either make x = '4' are actually give y a number value
"""

x = 'Hello'
y = 'World'
print x + y
"""
it runs and displays 'HelloWorld'
yes it works
"""

x = 'x'
y = 'x'
print x + y
"""
it runs and displays 'xx'
yes it works
"""

x = x
y = 'y'
print x + y
"""
there is a NameError
no it doesn't work
'x' isn't defined
we can give x the value of a string 'x'
"""

x = 'x'
y = x + 'y'
print x + y
"""
it runs and displays 'xxy'
yes it works
"""

x = 'Hello'
y = 4
print x / y
"""
there is a TypeError
no it doesn't work
with the division operator both values should be an int
change the value of x with a int value
"""

x = 'Hello'
y = 'World'
print x * y
"""
there is a TypeError
no it doesn't work
with the multiply operator both values should be an int
either change both x and y values to ints or change the operator to +
"""