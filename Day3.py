# given integral number n, create a dictionary with the function that creates the key value(n:n^2)
# integral is a number assigned to the function

print('Enter the number: ')
n = int(input())
d = dict()
for i in range(1, n+1):
    d[i] = i*i
print(d)