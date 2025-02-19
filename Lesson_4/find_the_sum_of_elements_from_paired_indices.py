import random

list_len = random.randint(0,20)
list_number = list()

for i in range(list_len):
    list_number.append(random.randint(0,20))

print(list_number)

tmp = 0
factor = list_number[-1] if len(list_number) >= 1 else 0

for i in list_number[::2]:
    tmp += i

print(tmp*factor)
