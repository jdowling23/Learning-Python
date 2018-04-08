# Find all the numbers divisible by 7 but not a multiple of 5 between 2000 and 3200
# solution should be comma seperated on a single line

empty_list = []

for i in range(2000, 3201):
    if (i%7 == 0) and (i%5 != 0):
        empty_list.append(str(i))

print(','.join(empty_list))