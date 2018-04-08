# List and Tuple creation
# List : mutable
# Tuple : immutable

values = input('Enter comma separated numbers:')
list = values.split(',')
tuple = tuple(list)
print(list, tuple)