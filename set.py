# list --> []
# tuple --> ()
# set --> {}

# set: unique items collection. No duplicate. 

numbers = [12, 56, 98, 56, 44, 88, 44, 36]
print(numbers)
numbers_set = set(numbers)
print(numbers_set)
numbers_set.add(55)
print(numbers_set)
# dont maintain order or sequence

numbers_set.remove(12)
print(numbers_set)

for item in numbers_set:
    print(item)


if 9 in numbers_set:
    print('9 exists')
elif 98 in numbers_set:
    print('98 exists')    



# methods --> len, issubset, issuperset, union, intersection

#union -- common in both
A = {1,3,5,7}
B = {1,2,3,4,5,6}

print( A & B)
print( A | B)