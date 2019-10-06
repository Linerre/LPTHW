i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}") # in order: 0, 1, 2, ... 5
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers) # [0], [0, 1], [0, 1, 2] ... [0, ..., 5]
    print(f"At the bottom i is {i}") # 1, 2, 3 ..., 6


print("The numbers: ")

for num in numbers:
    print(num)

# below is drills:
# drill 1:
i = 0
numbers = []
threshold = int(input('Please define the threshold using a whole number: '))

while i < threshold:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")


print("The numbers: ")

for num in numbers:
    print(num)

# drill 2:
i = 0
numbers = []
threshold = int(input('Please define the threshold using a whole number: '))
step = int(input('Enter a whole number for the increment at a time: '))

while i < threshold:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + step
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")


print("The numbers: ")

for num in numbers:
    print(num)
