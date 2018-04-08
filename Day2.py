# Compute the factorial of a given number. Result printed in csv single line
# recursive function
def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num-1)
print('Enter a number: ')
num = int(input())
print(factorial(num))