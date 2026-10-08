# def doubled(x):
#     return x*2

doubled = lambda num : num * 2
squared = lambda num : num * num 

result = doubled(44)
output = doubled(5)
# print (result, output)

add = lambda s, y : s+y
sum = add(11, 33)
# print(sum)


numbers = [12, 56, 98, 78, 56, 12, 26, 98]

# doubled_nums = map(doubled, numbers)
doubled_nums = map(lambda x: x*2, numbers)
squared_nums = map(lambda x: x*x, numbers)
# print(numbers)
# print(list(doubled_nums))
# print(list(squared_nums))


players = [
    {'name':'Messi', 'age': 39},
    {'name':'Ronaldino', 'age': 55},
    {'name':'Maradona', 'age': 65},
    {'name':'Ronaldo Nazario', 'age': 57},
    {'name':'Modric', 'age': 43},
    {'name':'Kaka', 'age': 52},
]

juniors = filter(lambda player: player['age'] > 45, players)
Fivers = filter(lambda player: player['age'] %5==0, players)
# print(list(juniors))
print(list(Fivers))