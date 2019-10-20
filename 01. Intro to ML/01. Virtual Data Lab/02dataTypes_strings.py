##############################
###### Strings ###############
##############################



# %% Single word
'hello'

# %% Entire phrase
'This is also a string'

# %% We can also use double quote
"String built with double quotes"


# %% Be careful with quotes!
' I'm using single quotes, but will create an error'



# %% 
"Now I'm ready to use the single quotes inside a string!"


# %% Output

# We can simply declare a string
'Hello World'

# note that we can't output multiple strings this way
'Hello World 1'
'Hello World 2'

# %% print
# We can use a print statement to print a string.

print('Hello World 1')
print('Hello World 2')
print('Use \n to print a new line')
print('\n')
print('See what I mean?')


# %% length of a string

len('Hello World')


# %% assign string to variables
# Assign s as a string
s = 'Hello World'

#Check
s

# Print the object
print(s)


# String indexing

# %% Show first element (in this case a letter)
s[0]

# %% Next element
s[1]

# %% Next Element
s[2]


# String indexing

# %% Grab everything past the first term all the way to the length of s which is len(s)
s[1:]


# %% Note that there is no change to the original s
s

# %% Grab everything UP TO the 3rd index
s[:3]


# Note the above slicing. Here we're telling Python to grab everything from
# 0 up to 3. It doesn't include the 3rd index. You'll notice this a lot in
# Python, where statements and are usually in the context of "up to, but not including".

# %% Everything
s[:]


# %% negative indexing 
s[-1]

# %% Grab everything but the last letter
s[:-1]


# We can also use index and slice notation to grab elements of a sequence by a
# specified step size (the default is 1). For instance we can use two colons in
# a row and then a number specifying the frequency to grab elements. For example:

# %% Grab everything, but go in steps size of 1
s[::1]

# %% Grab everything, but go in step sizes of 2
s[::2]

# %% We can use this to print a string backwards
s[::-1]

# %% 
a='01010101010101010101010101010'
a[::1] #step equal 1
a[::2] #step equal 2
a[1::2] #step equal 2 starting at first position

# %% String Properties
# Its important to note that strings have an important property known as
# immutability. This means that once a string is created, the elements within
# it can not be changed or replaced. For example:

s

# Let's try to change the first letter to 'x'
s[0] = 'x'


# Notice how the error tells us directly what we can't do,
# change the item assignment!
#
# %% Concatenate strings
s

# Concatenate strings!
s + ' concatenate me!'

# We can reassign s completely though!
s = s + ' concatenate me!'

print(s)

# %% repeat a string

letter = 'z'
letter*10


# %% string methods

# Upper Case a string
s.upper()

# Lower case
s.lower()

# Split a string by blank space (this is the default)
s.split()

# Split by a specific element (doesn't include the element that was split on)
s.split('W')

# Remove final empty spaces
sss="asdfkjhasf                    "
print(f"String sss has len {len(sss)}")

sss=sss.strip()
print(sss)
print(f"String sss has len {len(sss)}")



# %% stirng formatting
# We can use the .format() method to add formatted objects to printed string statements.
#
# The easiest way to show this is through an example:

'Insert another string with curly brackets: {}'.format('The inserted string')

# Using the string .format() method
# The best way to format objects into your strings for print statements is using
# the format method. The syntax is:
#
#  'String here {var1} then also {var2}'.format(var1='something1',var2='something2')
#
# Lets see some examples:


print('This is a string with an {p}'.format(p='insert'))

# Multiple times:
print('One: {p}, Two: {p}, Three: {p}'.format(p='Hi!'))


# Several Objects:
print('Object 1: {a}, Object 2: {b}, Object 3: {c}'.format(a=1,b='two',c=12.3))


# That is the basics of string formatting!
# Often we'll use the simpler form with f-string literals (MUST USE PY 3.6 FOR THIS)
username = "Jose"
color = "Blue"
print(f"The name is {username} and color is {color}")
# %% exercise
#1 create a dynamic string to say welcome to different users of a website
