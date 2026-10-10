n = int(input())
a = input().split()

# convert every item to int
nums = []
for item in a:
    nums.append(int(item))

operations = 0

while True:
    # check if all numbers are even
    all_even = True
    for x in nums:
        if x % 2 != 0:
            all_even = False
            break

    if all_even == False:
        break        # found an odd number, stop

    # all are even, so divide each one by 2
    for i in range(n):
        nums[i] = nums[i] // 2

    operations = operations + 1

print(operations)