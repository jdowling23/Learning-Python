# create a class with 2 methods
# 1. get_string: gets string from input
# 2. print_string: prints string

class in_out(object):
    def __init__(self):
        self.s = ''
    def get_string(self):
        self.s = input('Give me a string...')
    def print_string(self):
        print(self.s.upper())

x = in_out()
print(x)
# calling a class will print in_out memory location
# if i want to actually execute the methods from class i need to call them

x.get_string()
x.print_string()