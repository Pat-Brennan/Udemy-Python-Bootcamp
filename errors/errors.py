
# * Common Errors!

# * Syntax Error
# ? Occurs when python encounters incorrect syntax(something it doesn't parse)
# ? Usually due to typos or not knowing python well enough

# * Name Error
# ? This occurs when a variable is not defined, i.e it has not been assigned

# * Type Error
# ? An operation or function is applied to the wrong data type
# ? Python cannot interpret an operation on two data types

# len(5) 'Object of type int has no len'

# * Index Error
# ? Occurs when you try to access an element in a list using an invalid index
# ? (i.e one that is outside the range of the list or string)

# list = ['hey there']
# list[2]
# ERROR: list index out of range

# * Value Error
# ? This occurs when a built-in operation or function receives an argument
# ? that has the right type but an inappropriate value.

# int('foo')
# ValueError: The fact that it's a string isn't the problem... it's that it doesn't specify a number

# * Key Error
# ? This occurs when a dictionary does not have a specific key
# ? Much like an index error for lists

# d= {}
# d['foo']
# KeyError: 'foo'

# * Attribute Error
# ? This occurs when a variable does not have an attribute.

# 'awesome'.foo
# AttributeError: 'str' object has no attribute 'foo'

# ! When in doubt, just google the error!