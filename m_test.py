import random




letters = ["a", "b", "c", "d"]
numbers = ["0" ,"1", "2", "3", "4", "5"]

random.shuffle(numbers)
random.shuffle(letters)

l = []

for i in range(3):
    l.append(numbers[i])
    l.append(letters[i])




result = "".join(l)


for i in range(10):
    print(result)
