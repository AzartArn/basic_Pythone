import random

list_len = random.randint(3,10)
list_number = list()
list_new = list()

for i in range(list_len):
    list_number.append(random.randint(0,20))

print(list_number)

list_new.append(list_number[0])
list_new.append(list_number[2])
list_new.append(list_number[-2])

print(list_new)