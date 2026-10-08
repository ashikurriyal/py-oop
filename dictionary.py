numbers = [12, 56, 98, 78, 56, 12, 26, 98]
# key value pair
# dictionary
# hash table
# overlap with set
# {key: value, key: value}
person = {'name': "ashik", 'address': 'badda', 'age': '26', 'job': 'developer'}
print(person)
print(person['job'])
print(person.keys())
print(person.values())

# i can add that means it is mutable

person['language'] = 'python'
print(person)
person['name'] = 'Ashikur Rahman'
print(person)

# only key
for item in person:
    print(item)

# special looping in dictionary
for key, value in person.items():
    print(key, value)